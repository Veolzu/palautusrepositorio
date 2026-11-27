import re

from matchers import QueryBuilder, Not


_TOKEN_PATTERN = re.compile(r"\s*(>=|=|<|[A-Za-z_][A-Za-z0-9_]*|-?\d+)")


class _Parser:
    def __init__(self, query):
        self._tokens = self._tokenize(query)
        self._position = 0

    def _tokenize(self, query):
        query = query.strip()
        tokens = []
        position = 0

        while position < len(query):
            match = _TOKEN_PATTERN.match(query, position)
            if match is None:
                raise ValueError(f"Virheellinen kysely kohdassa {position}: {query!r}")

            tokens.append(match.group(1))
            position = match.end()

        return tokens

    def parse(self):
        if not self._tokens:
            raise ValueError("Kysely ei voi olla tyhjä")

        groups = [self._parse_and_group()]
        while self._accept("or"):
            groups.append(self._parse_and_group())

        if self._position < len(self._tokens):
            raise ValueError(f"Odottamaton token: {self._peek()}")

        if len(groups) == 1:
            return groups[0].build()

        return QueryBuilder().one_of(*groups).build()

    def _parse_and_group(self):
        builder = QueryBuilder()
        builder = self._add_condition(builder)

        while self._accept("and"):
            builder = self._add_condition(builder)

        return builder

    def _add_condition(self, builder):
        negate = False
        while self._accept("not"):
            negate = not negate

        attribute, operator, value = self._parse_predicate()
        if negate:
            condition = _add_to_builder(QueryBuilder(), attribute, operator, value).build()
            return builder.not_(condition)

        return _add_to_builder(builder, attribute, operator, value)

    def _parse_predicate(self):
        attribute = self._consume_value("attribuutti")
        operator = self._consume_value("vertailuoperaattori")
        value = self._consume_value("arvo")

        if operator not in ("=", ">=", "<"):
            raise ValueError(f"Tuntematon vertailuoperaattori: {operator}")
        if self._is_keyword(value):
            raise ValueError(f"Virheellinen vertailuarvo: {value}")

        if attribute == "team":
            if operator != "=" or value.lstrip("-").isdigit():
                raise ValueError("team-attribuutin tukema ehto on 'team = XXX'")
        else:
            if operator == "=" or not value.lstrip("-").isdigit():
                raise ValueError("Numeerinen attribuutti vaatii ehdon >= tai < ja luvun")
            value = int(value)

        return attribute, operator, value

    def _consume_value(self, expected):
        if self._position >= len(self._tokens):
            raise ValueError(f"Kyselystä puuttuu {expected}")

        value = self._tokens[self._position]
        self._position += 1
        return value

    def _accept(self, token):
        if self._peek() == token:
            self._position += 1
            return True
        return False

    def _peek(self):
        if self._position >= len(self._tokens):
            return None
        return self._tokens[self._position]

    @staticmethod
    def _is_keyword(value):
        return value in ("and", "or", "not")


def _add_to_builder(builder, attribute, operator, value):
    if attribute == "team":
        return builder.plays_in(value)
    if operator == ">=":
        return builder.has_at_least(value, attribute)
    return builder.has_fewer_than(value, attribute)


def parse(query):
    """Parse a query-language string into a matcher."""
    if not isinstance(query, str):
        raise ValueError("Kyselyn tulee olla merkkijono")

    return _Parser(query).parse()
