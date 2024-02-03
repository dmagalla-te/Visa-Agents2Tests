from Operations import read_files, get_info, agents2Tests, provision_agents



def main(directory_path):

    # primero leemos test -- agents



    """
    #obtenemos info de TE
    te_agents, te_tests = get_info(OAUTH="7c94c90e-b5d3-4bf5-8801-403b76c32e42")

    print(te_agents)
    print(te_tests)

    #leer jsons para obtener toda la info guardada
    cvs_agents = read_files(directory_path)


    # we update the te_tests dictionary to include a list of the agents that will be added 
    te_tests = agents2Tests(te_tests, te_agents, cvs_agents)

    provisioning = provision_agents(te_tests, OAUTH="")

    return provisioning


print(main(directory_path="cvs_folder/"))"""

main(main(directory_path="/"))