from database.concepts import repository


def start_and_clear_for_test():
    repository.Repository()  # start engine and establish connection
    repository.Base.metadata.drop_all(
        repository.Repository.get_engine()
    )  # clear from previous tests data
    repository.Base.metadata.create_all(repository.Repository.get_engine())
