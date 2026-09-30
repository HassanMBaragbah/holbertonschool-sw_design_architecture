#!/usr/bin/env python3
class Beverage:
    def cost(self) -> int:
        raise NotImplementedError

    def description(self) -> str:
        raise NotImplementedError


class Coffee(Beverage):
    def cost(self) -> int:
        return 50

    def description(self) -> str:
        return "Coffee"


class BeverageDecorator(Beverage):
    def __init__(self, inner: Beverage) -> None:
        self._inner = inner

    def cost(self) -> int:
        return self._inner.cost()

    def description(self) -> str:
        return self._inner.description()


class MilkDecorator(BeverageDecorator):
    def cost(self) -> int:
        return self._inner.cost() + 10

    def description(self) -> str:
        return self._inner.description() + " + milk"


class SugarDecorator(BeverageDecorator):
    def cost(self) -> int:
        return self._inner.cost() + 5

    def description(self) -> str:
        return self._inner.description() + " + sugar"


class CaramelDecorator(BeverageDecorator):
    def cost(self) -> int:
        return self._inner.cost() + 15

    def description(self) -> str:
        return self._inner.description() + " + caramel"


def main() -> None:
    bev1 = MilkDecorator(Coffee())
    print(f"{bev1.description()} {bev1.cost()}")

    bev2 = MilkDecorator(SugarDecorator(Coffee()))
    print(f"{bev2.description()} {bev2.cost()}")

    bev3 = CaramelDecorator(MilkDecorator(SugarDecorator(Coffee())))
    print(f"{bev3.description()} {bev3.cost()}")


if __name__ == "__main__":
    main()
