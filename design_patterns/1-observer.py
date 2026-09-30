#!/usr/bin/env python3
from typing import Dict, Optional, Set


class Observer:
    def update(self, topic: str, data: str) -> None:
        raise NotImplementedError


class NewsSubject:
    def __init__(self) -> None:
        self._subscribers: Dict[Observer, Optional[Set[str]]] = {}

    def subscribe(
        self, observer: Observer, topics: Optional[Set[str]] = None
    ) -> None:
        self._subscribers[observer] = topics

    def unsubscribe(self, observer: Observer) -> None:
        self._subscribers.pop(observer, None)

    def notify(self, topic: str, data: str) -> None:
        # Snapshot iteration to safely handle modifications during broadcast
        for observer, topics in list(self._subscribers.items()):
            if topics is None or topic in topics:
                observer.update(topic, data)


class LogObserver(Observer):
    def update(self, topic: str, data: str) -> None:
        print(f"log:{topic}={data}")


class EmailObserver(Observer):
    def update(self, topic: str, data: str) -> None:
        print(f"email:{topic}={data}")


class SmsObserver(Observer):
    def update(self, topic: str, data: str) -> None:
        print(f"sms:{topic}={data}")


def main() -> None:
    subject = NewsSubject()

    log_obs = LogObserver()
    email_obs = EmailObserver()
    sms_obs = SmsObserver()

    # LogObserver listens only to "sports" and "breaking"
    subject.subscribe(log_obs, topics={"sports", "breaking"})
    # EmailObserver listens to all topics (topics=None)
    subject.subscribe(email_obs)
    # SmsObserver listens only to "breaking"
    subject.subscribe(sms_obs, topics={"breaking"})

    subject.notify("weather", "rain")
    subject.notify("sports", "goal")
    subject.notify("breaking", "alert")


if __name__ == "__main__":
    main()
