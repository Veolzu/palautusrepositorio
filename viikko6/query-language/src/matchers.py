class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value

class All:
    def __init__(self):
        pass

    def test(self, players):
        return True


class Not:
    def __init__(self, result):
        self._result = result

    def test(self, player):
        return not self._result.test(player)

class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True

        return False


class QueryBuilder:
    def __init__(self, build_query=All):
        self._build_query = build_query

    def plays_in(self, team):
        def build_play_in_query():
            query = self._build_query()
            return And(query, PlaysIn(team))
        return QueryBuilder(build_play_in_query)

    def has_at_least(self, val, attr):
        def build_has_at_least_query():
            query = self._build_query()
            return And(query, HasAtLeast(val, attr))
        return QueryBuilder(build_has_at_least_query)

    def has_fewer_than(self, val, attr):
        def build_has_fewer_than_query():
            query = self._build_query()
            return And(query, HasFewerThan(val, attr))
        return QueryBuilder(build_has_fewer_than_query)

    def one_of(self, *queries):
        def build_or_queries():
            current_query = self._build_query()
            alternatives = [query.build() for query in queries]
            return And(current_query, Or(*alternatives))

        return QueryBuilder(build_or_queries)

    def not_(self, matcher):
        def build_not_query():
            query = self._build_query()
            return And(query, Not(matcher))

        return QueryBuilder(build_not_query)


    def build(self):
        return self._build_query()
