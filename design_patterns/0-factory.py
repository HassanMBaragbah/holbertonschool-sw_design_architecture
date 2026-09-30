#!/usr/bin/env python3
from typing import Dict, Type


class Vehicle:
    def mode(self) -> str:
        raise NotImplementedError


class Bus(Vehicle):
    def mode(self) -> str:
        return "road"


class Train(Vehicle):
    def mode(self) -> str:
        return "rails"


class Bike(Vehicle):
    def mode(self) -> str:
        return "lane"


class Scooter(Vehicle):
    def mode(self) -> str:
        return "scooter_lane"


class VehicleFactory:
    def __init__(self) -> None:
        self._registry: Dict[str, Type[Vehicle]] = {}

    def register_kind(self, name: str, cls: Type[Vehicle]) -> None:
        self._registry[name] = cls

    def create(self, kind: str) -> Vehicle:
        if kind not in self._registry:
            raise ValueError(f"Unknown vehicle kind: {kind}")
        return self._registry[kind]()


def main() -> None:
    factory = VehicleFactory()
    factory.register_kind("bus", Bus)
    factory.register_kind("train", Train)
    factory.register_kind("bike", Bike)

    # Registering Scooter dynamically without modifying VehicleFactory.create
    factory.register_kind("scooter", Scooter)

    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())
    print(factory.create("scooter").mode())


if __name__ == "__main__":
    main()
