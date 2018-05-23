# ######################################################################################################################
#
# ######################################################################################################################


def home(session, g, request):
    return True


def home_vm(session, g, request):
    vm = lambda: None

    vm.username = session["username"]

    return vm


def inventory(session, g, request):
    return True


def shopping(session, g, request):
    return True
