from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

from sqlmodel import SQLModel
from app.core.config import settings

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

#config.set_main_option("sqlalchemy.url", settings.alembic_database)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata

# Barrido
from app.model.barrido.barrido import Barrido
from app.model.barrido.usuario_barrido import UsuarioBarrido

#Recoleccion
from app.model.recoleccion.recoleccion_particular import RecoleccionParticular
from app.model.recoleccion.recoleccion import Recoleccion
from app.model.recoleccion.usuario_recoleccion import UsuarioRecoleccion
from app.model.recoleccion.vehiculo import Vehiculo

#Residuo
from app.model.residuo.tipo_residuo import TipoResiduo

#Ruta
from app.model.ruta.ruta import Ruta
from app.model.ruta.tipo_ruta import TipoRuta
from app.model.ruta.punto_recoleccion_ruta import PuntoRecoleccionRuta
from app.model.ruta.punto_recoleccion import PuntoRecoleccion

#Usuario
from app.model.usuario.rol import Rol
from app.model.usuario.usuario import Usuario
from app.model.usuario.users import Users

from app.model.table_base import TableBase
target_metadata = SQLModel.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


from sqlmodel import create_engine

def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = create_engine(
        settings.database_url
        #target_metadata=target_metadata
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
