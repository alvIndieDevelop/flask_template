from app.main import create_app

import os
app = create_app(os.getenv('CONFIG_ENV') or 'dev')


def run():
    port=int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    run()