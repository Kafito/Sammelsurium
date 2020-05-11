# lacl
Launch And Control Later - a pure bash process launcher that allows for deferred terminal connections via built-in facilities.

## Motivation
lacl was inspired by the need to launch processes as services, e.g. via systemd,
that are rather meant to be run as a foreground shell process. Common
workarounds use tools like tmux or screen to launch the process and control it
later.  To me this always seemed to be unintuitive and an overkill, so -- out of
curiosity -- I started experimenting with bash scripts without dependencies to
solve this problem, and continue to do so in this repository.

## What lacl does
- Allows you to launch a process in the background.
- Allows you to connect to the commandline of said background process later to
  issue commands.
- Issue commands by simply writing to a fifo, useful for writing server bots.
- Retrieve the output of said command manually by inspecting a usual log file.
- Option to gracefully shut down processes with commands on SIGTERM (useful for
  Systemd services, for example).

## What lacl does not
- It can not provide a fully fledged command line (there are problems with
  back-space, for example).
- TODO: Add more technical details here.

## Usage
```
    $ lacl start token [--stopsequence seq] command arg1 arg2 ...
    $ lacl connect token
    $ lacl stop token
    $ lacl kill token
```

For all cases, `token` is a user provided identifier for the background task,
necessary to connect to and stop the background service.

`lacl start` will start a background subshell that executes `command` with the
given arguments `arg1 arg2 ...`. `--stopsequence seq` defines a character
sequence that will be send to the input stream of the process when the process
group receives `SIGTERM`. This is quite useful to gracefully shut down a process
that reacts on "quit" or "exit" or similar commands. If set, the process
`command` is set to ignore `SIGTERM`.

You can connect to this process by starting the provided commandline frontend
via `lacl connect token`.

`lacl stop` or `lacl kill` will end the given process with `SIGTERM` or
`SIGKILL`, respectively.

## Files
When a process with a given `token` is started, `lacl` creates three files:
* `/dev/shm/token.log`, which contains the output of the started process.
* `/dev/shm/token.ctl`, the fifo that can be used to control the process.
* `/dev/shm/token.pid`, containing pid information on the started processes.

## Dependencies
* bash
* kill

## Alternatives
- [tmux](https://github.com/tmux/tmux) /
  [screen](http://www.gnu.org/software/screen) /
  [dtach](https://github.com/crigler/dtach) or any other pty implementation.
- reset/modify file descriptors of the process by attaching gdb and using its
  facilities.
- Use tools such as [screenify](http://sooda.dy.fi/foo/screenify),
  [retty](http://manpages.ubuntu.com/manpages/precise/man1/retty.1.html) or
  [reptyr](https://github.com/nelhage/reptyr) to modify or attach to the
  controlling terminals of the process.

## License
This project is licensed under the MIT License - see the
[LICENSE.txt](LICENSE.txt) file for details
