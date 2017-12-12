# -*- coding: utf-8 -*-


# This is Main module for ExampleProject that do nosting.


def Confluence():
    """
    This is Main method that do nosting.
    """
    return "This is Main module for Confluence Project that do nothing.\nRead more about DevOpsHQ Community here: https://github.com/devopshq/ExampleProject"


if __name__ == "__main__":
    print(Main())

    import pkg_resources  # part of standart setuptools
    print("Version of Confluence is [ {} ]".format(pkg_resources.get_distribution('dohq-confluence').version))
