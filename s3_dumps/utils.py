import os

def init_arguments(parser):
    SERVICE_NAME = os.environ.get('SERVICE_NAME')
    ACCESS_KEY = os.environ.get('ACCESS_KEY')
    SECRET = os.environ.get('SECRET')


    parser.add_argument('--SERVICE_NAME', 
        required=SERVICE_NAME is None,
        default=SERVICE_NAME,
        help='''Supported Amazon/ DigitalOcean Services Eg. amazon or
            digitalocean ( field is required if not defined in SERVICE_NAME
            environment variable )''')

    parser.add_argument('--ACCESS_KEY',
        required=ACCESS_KEY is None,
        default=ACCESS_KEY,
        help='''Access key ( field is required if not defined in ACCESS_KEY
            environment variable )''')

    parser.add_argument('--SECRET',
        required=SECRET is None,
        default=SECRET,
        help='''Secret key (required if not defined in SECRET environment
            variable)''')

    parser.add_argument('--BUCKET_NAME',
        required=True, 
        help='Bucket name')

    parser.add_argument('--FILE_KEY', 
        required=True,
        help='''The directory path where you want to put dump
            (i.e. backups/postgres/server_name)''')

    parser.add_argument('--REGION',
        default='',
        help='s3 region Eg. us-east-1 (default is set to "")')

    parser.add_argument('--DB_NAME',
        required=False,
        help='''The database you want to backup (i.e. my_database).
            If DB_NAME not provided then it dumps all databases.''')

    parser.add_argument('--POSTGRES_DUMP_CMD',
        default='pg_dump',
        help='''Path to pg_dumpall (default: pg_dump).
            You may change according to system Eg. /usr/bin/pg_dump''')

    parser.add_argument('--DUMP_BASE_DIR',
        default='',
        help='Path to dumps directory (default: "")')

    parser.add_argument('--DELETE_DUMP',
        default=True,
        help='''Boolean value if True deletes the dump file from
            dumps base directory''')

    parser.add_argument('--DUMP_RDB_PATH',
        default='/var/lib/redis/dump.rdb',
        help='''The path to the Redis dump.rdb file 
            (default: /var/lib/redis/dump.rdb)''')

    parser.add_argument('--REDIS_SAVE_CMD',
        default='/usr/bin/redis-cli SAVE',
        help='''Command to save the Redis DB to disk
        (default: /usr/bin/redis-cli SAVE)''')

    parser.add_argument('-v', '--verbose',
        default=True,
        action='store_true',
        help='Verbose')

    parser.add_argument('--backup',
        action='store_true',
        help='Backup up Postgres to S3')

    parser.add_argument('--archive',
        action='store_true',
        help='Backup up Postgres to S3')

    return parser


def init_logger(logger):
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
