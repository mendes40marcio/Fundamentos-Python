import logging
from rich.logging import RichHandler


def configurar_logger():
    logging.basicConfig(
        level=logging.INFO,
        handlers=[RichHandler()]
    )
    return logging.getLogger("app")


def conectar_banco():
    # simulando uma falha
    raise ConnectionError("Banco de dados indisponível")


def main():
    log = configurar_logger()

    log.info("Aplicação iniciada")

    try:
        conectar_banco()
        log.info("Conectado ao banco com sucesso")
    except ConnectionError as erro:
        log.error(f"Erro ao conectar ao banco: {erro}")

    log.warning("Modo desenvolvimento ativo")


if __name__ == "__main__":
    main()
