load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_python",
    sha256 = "778aaeab3e6cfd56d681c89f5c10d7ad6bf8d2f1a72de9de55b23081b2d31618",
    strip_prefix = "rules_python-0.34.0",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.34.0/rules_python-0.34.0.tar.gz",
)


load("@rules_python//python:repositories.bzl", "py_repositories")

py_repositories()

# Load pip requirements
load("@rules_python//python:pip.bzl", "pip_parse")

pip_parse(
   name = "notebooks",
   requirements_lock = "//notebooks:requirements.txt",
)

load("@notebooks//:requirements.bzl", "install_deps")

install_deps()