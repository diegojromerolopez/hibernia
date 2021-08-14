from typing import Optional

from gelidum.collections import frozendict


class KVStore(object):
    def __init__(self):
        self.__store = frozendict({})

    def set(self, key: str, val: str) -> bool:
        if val is None:
            return False
        self.__store = self.__store + frozendict({key: val})
        return True

    def get(self, key: str) -> Optional[str]:
        return self.__store.get(key)

    def del_item(self, key: str) -> bool:
        if key in self.__store:
            self.__store = frozendict(
                {k: v for k, v in self.__store.items() if k != key}
            )
            return True
        return False


KV_STORE = KVStore()
