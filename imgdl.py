import configuration


def main():
    config = configuration.Config()
    settings = config.get_settings()
    services = config.get_services()
    print(settings)
    print(services)


if __name__ == "__main__":
    main()
