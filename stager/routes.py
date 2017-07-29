from docopt import docopt
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import system_information as sysinf
import json

class routing():

    def getroute(data_param):

        # Instantiate Flask app
        app = Flask(__name__, static_url_path='/static')

        data = data_param

        # Routing
        #   Root
        @app.route('/')
        def welcome():
            return render_template('formtemplate_vue.html', sysinf=data.inf, gentooModel=data.gentooModel)

        #   Gentoo Form
        @app.route('/form')
        def formtest():
            return render_template('formtemplate_vue.html', sysinf=data.inf, gentooModel=data.gentooModel)


        @app.route('/ajax/pullpartitions', methods=['GET', 'POST'])
        def pullpartitions():

            parts = []

            if request.method == 'GET':
                index = int(request.args.get('disk'))
            else:
                index = int(request.form.getlist('part')[0])

            returned_parts = sysinf.getPartitions(index)

            for part in returned_parts:
                print(part)
                parts.append({"number": part.number, "path": part.path, "name": part.name, "type": part.type, "active": part.active, "busy": part.busy, "part_geom_start": part.geometry.start, "part_geom_end": part.geometry.end, "part_geom_length": part.geometry.length, "disk_geom_length": part.disk.device.length, "sector_size": part.disk.device.sectorSize})

            return json.dumps(parts)


        #    Auth
        @app.route('/auth', methods=['GET', 'POST'])
        def login(self, app):
            print ('auth page')
            error = None
            if request.method == 'POST':
                if request.form['password'] != app.config['PASSWORD']:
                    error = 'Invalid authorization key'
                else:
                    session['logged_in'] = True
                    flash('Session has been authenticated!')
                    return redirect(url_for('show_entries'))
            return render_template('login.html', error=error)

        if __name__ == '__main__':
            arguments = docopt(__doc__, version=__version__)
            print (arguments)

        # Run app
        app.run(debug=True)
