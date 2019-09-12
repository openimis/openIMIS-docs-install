#
# This file generates the sidebar/toctree for all RobotPy projects and should
# be copied to each project when it is updated
#

import os


def write_if_changed(fname, contents):

    try:
        with open(fname, "r") as fp:
            old_contents = fp.read()
    except:
        old_contents = ""

    if old_contents != contents:
        with open(fname, "w") as fp:
            fp.write(contents)


def generate_sidebar(conf, conf_api):

    # determine 'latest' or 'stable'
    # if not conf.do_gen:
    do_gen = os.environ.get("SIDEBAR", None) == "1" or conf["on_rtd"]
    version = conf["rtd_version"]

    lines = ["", ".. DO NOT MODIFY! THIS PAGE IS AUTOGENERATED!", ""]

    def toctree(name):
        lines.extend(
            [".. toctree::", "    :caption: %s" % name, "    :maxdepth: 2", ""]
        )

    def endl():
        lines.append("")

    def write(desc, link):
        if desc != conf["subproject"] :
            args = desc, link
        elif not do_gen:
            return
        else:
            args = (
                desc,
                "https://openimis.readthedocs.io/en/%s/%s.html" % (version, link),
            )

        lines.append("    %s <%s>" % args)

    def writeProject(desc, link):
        if desc != conf["subproject"] :
            args = desc, link
        elif not do_gen:
            return
        else:
            args = (
                desc,
                "https://openimis.readthedocs.io/Projects/%s/%s/" % (link, version),
            )

        lines.append("    %s <%s>" % args)

    toctree("OpenIMIS")
    write("User manual", "index")
    writeProject("Install manual", "install")
    endl()

    write_if_changed("_sidebar.rst.inc", "\n".join(lines))