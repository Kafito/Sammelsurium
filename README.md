# RealStaticPicoCMS
RealStaticPicoCMS - serving "static" as in "aesthetic"

A script that avoids the "dynamically serving static files" approach of
of Pico (http://github.com/picocms/Pico.git).

This script will start Pico in a temporary web server, extract all files
of the homepage and store them as .html files in a local directory that can
be served statically.

It can be called in the context of inotify to rebuild the homepage, when a
new file is added to the content directory of Pico.

## How to Run:
This tool currently not fully flexible, and an adaption to its source is most
likely necessary. It is advised to read through the source code (which is not
much) and carefully inspect the results before running it in an productive
environment (if at all).
Other than that:
```
    $ realstaticpicocms
```
It currently outputs the status for each files it fetches from the webserver
(in addition to the output of the webserver), which usually is enough for
checking and debugging whether / how it works.

## Motivation:
RealStaticPicoCMS was inspired by inspecting how the
[NextCloud](https://nextcloud.com) plugin [Nextcloud CMS
Pico](https://github.com/nextcloud/cms_pico) works internally. While being a
comfortable way of creating a website, I was surprised to see that the
so-called "static" files were still served dynamically. Also, the underlying
software, [Pico](http://picocms.org) is instantiated per access to the
website. This may eventually lead to scalability issues.

Additionally, it appeared to be quite a hassle to configure the webserver
rewrites/redirects for something that should be trivial (i.e. a static
website).

While there are tools that help building a real static website (see
[Alternatives](#alternatives)), I decided to work on this nevertheless, for the
following reasons:
* out of curiosity
* to be able to serve a previously configured setup (themes, ...) without
  modifications.
* to continue working in a comfortable way via Nextcloud: Just upload a file
  and it is served automatically. This can be achieved by pairing this script
  with inotify.

## Limitations:
* Currently, assets and themes are not handled. These need to be copied manually.
* The static files are stored as ".html" files, but links within Pico are provided
  without a suffix. This can be changed by adapting the .twig files of the theme.

## Disclaimer:
Currently users of this file most likely will need to adapt not
only the config variables, but the code was well, as it is tuned for the
website the author was working on.

## Alternatives
There many tools that really build static files out of markdown files, for example:
* [Jekyll](https://jekyllrb.com)
* [Hugo](https://gohugo.io)
Or pick any other tool listed on https://www.staticgen.com.
