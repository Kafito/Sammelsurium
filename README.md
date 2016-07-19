# lacl
Launch And Control Later - a pure bash process launcher that allows for deferred terminal connections via built-in facilities

## Motivation
lacl was inspired by the need to launch services, e.g. via systemd, that are rather meant to be run as a foreground shell process. Usually, tools like tmux or screen are used to launch the process and control it later, but conceptually this has always appeared to be a workaround to me.
Out of curiosity I started experimenting with bash scripts without dependencies to solve this problem, and continue to do so in this repository.

## What lacl does
- Allows you to launch a process in the background.
- Allows you to connect to the commandline of said background process later to issue commands.
- Issue commands by simply writing to a fifo, useful for writing server bots.

## What lacl does not
- It can not provide a fully fledged command line, there are problems with back-space.
- TODO: Add more technical details here.

## Usage
    lacl start token command arg1 arg2
    lacl connect token
    lacl stop token

## Alternatives
- tmux / screen
- complete virtual terminals (TODO: find links).
