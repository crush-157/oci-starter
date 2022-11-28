#!/usr/bin/env python3
# OCI Starter
# 
# Script to create an OCI deployment scaffold with application source code
# 
# Authors: Marc Gueury & Ewan Slater
# Date: 2022-11-24
import sys, os

# constants
ABORT='ABORT'
GIT='GIT'
CLI='CLI'

# functions
def title():
    s = "-- " + script_name() + " "
    return s.ljust(78,'-')

def script_name():
    return os.path.basename(__file__)

def get_mode():
    n_args=len(sys.argv)
    if n_args < 4:
        return ABORT
    elif n_args == 4:
        return GIT
    else:
        return CLI

def prog_arg_list():
    arr = sys.argv.copy()
    arr.pop(0)
    return arr

def prog_arg_dict():
    return list_to_dict(prog_arg_list())

mandatory_options = ['-language','-deploy','-db_password']

default_options = {
    '-prefix': 'starter',
    '-java_framework': 'helidon',
    '-java_vm': 'jdk',
    '-java_version': 17,
    '-kubernetes': 'oke',
    '-ui': 'html',
    '-database': 'atp',
    '-db_user': 'admin'
}

no_default_options = ['-compartment_ocid', '-oke_ocid', '-vcn_ocid', \
    '-atp_ocid', '-db_ocid', '-mysql_ocid']

# conditional_options specified as <K,V> pairs where
# K = option
# V = option it depends on
conditional_options = {
    '-subnet_ocid': '-vcn_ocid'
}

def allowed_options():
    return list(default_options.keys()) \
        + list(conditional_options.keys()) \
        + mandatory_options + no_default_options

def help():
    message = f'''
Usage: {script_name()} [OPTIONS]

oci-starter.sh
   -prefix (default starter)
   -compartment_ocid (default tenancy_ocid)
   -language (mandatory) java | node | python | dotnet | ords 
   -deploy (mandatory) compute | kubernetes | function
   -java_framework (default helidon | springboot | tomcat)
   -java_vm (default jdk | graalvm)  
   -java_version (default 17 | 11 | 8)
   -kubernetes (default oke | docker) 
   -oke_ocid ()
   -ui (default html | reactjs | jet | angular | none) 
   -vcn_ocid()
   -subnet_ocid()
   -database (default atp | dbsystem | mysql)
   -atp_ocid (optional)
   -db_ocid (optional)
   -mysql_ocid (optional)
   -db_user (default admin)
   -db_password ( mandatory )
'''
    if len(unknown_params) > 0:
        print('U')
        s = ' '
        for unknown in unknown_params:
            s += f'{unknown} '
        message += f'unknown parameter(s):{s}\n'
    if len(missing_params) > 0:
        print('M')
        s = ' '
        for missing in missing_params:
            s += f'{missing} '
        message += f'missing parameter(s):{s}\n'
    if len(missing_conditional_params) > 0:
        print('C')
        s = ' '
        for key in missing_conditional_params:
            s += f'{missing_conditional_params[key]} is mandatory with {key}\n'
        message += f'missing parameters:{s}\n'
    return message

def list_to_dict(a_list):
    it = iter(a_list)
    res_dct = dict(zip(it, it))
    return res_dct

def deprefix_keys(a_dict, prefix_length = 1):
    return dict(map(lambda x: (x[0][prefix_length:],x[1]),a_dict.items()))

def missing_parameters(supplied_params, expected_params):
    expected_set = set(expected_params)
    supplied_set = set(supplied_params)
    for supplied in supplied_set:
        expected_set.discard(supplied)
    return list(expected_set)

def cli_params():
    return deprefix_keys(default_options | prog_arg_dict())

def git_params():
    keys = ['git_url', 'repository_name', 'oci_username']
    values = prog_arg_list()
    return dict(zip(keys, values))

def missing_conditional_parameters():
    missing_pairs = {}
    for key in conditional_options:
        if prog_arg_dict().get(key) is not None:
            if prog_arg_dict().get(conditional_options[key]) is None:
                missing_pairs[key] = conditional_options[key]
    return missing_pairs

# the script
print(title())

script_dir=os.getcwd()

mode = get_mode()

missing_params = []
unknown_params = []

if mode == CLI:
    missing_params = missing_parameters(prog_arg_dict().keys(), mandatory_options)
    unknown_params = missing_parameters(allowed_options(), prog_arg_dict().keys())
    missing_conditional_params = missing_conditional_parameters()
    if len(missing_params) > 0 or len(unknown_params) > 0 or len(missing_conditional_params) > 0:
        mode = ABORT
    else:
        params = cli_params()

if mode == GIT:
    params = git_params()

if mode == ABORT:
    print(help())
    exit()

print(f'Mode: {mode}')
print(f'params: {params}')
print("That's all Folks!")