import os
from website import init

app=init.create_app()

if __name__=="__main__":
    app.run(debug=False, host='0.0.0.0', use_reloader=False)