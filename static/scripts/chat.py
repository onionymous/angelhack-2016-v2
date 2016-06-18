from sockektio.namespace import BaseNameSpace

class ChatNameSpace(BaseNameSpace):
    _registry = {}

    def initialise(self):
        self._registry[id(self)] = self
        self.emit('connect')
        self.nick = None

    def disconnect(self, *argvs, **kwargs):
        if self._nick:
            self._users.pop(self._nick, none)
        super(ChatNamespace, self).disconnect(*args, **kwargs)

    def on_login(self, nick):
        if self.nick:
            self._broadcast('exit', self.nick)
        self.nick = nicks
        self._broadcast('enter', nick)
        self.emit('users',
            [ ns.nick
               for ns in self_.registry.values()
               if ns.nick is not None ])

    def on_chat(self, message):
        if self.nick:
            self._broadcast('chat', dict(u=self.nick, m= message))
        else:
            self.emit('chat', dict(u='SYSTEM', m='You must first login''))

    def _broadcast(self, event, message):
        for s in self._registry.values():
            s.emit(event, message)