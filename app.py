

import openshift as oc

if __name__ == '__main__':
    with oc.tracking() as tracker:
        try:
            print('Current project: {}'.format(oc.get_fields()))
            print('Current user: {}'.format(oc.whoami()))
        except:
            print('Error acquire details about project/user')


