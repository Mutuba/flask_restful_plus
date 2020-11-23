# from flask import Flask

# FILE_FOLDER = 'path/to/file_folder'
# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = FILE_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024



# in another file

# from backend import ALLOWED_EXTENSIONS, app, FILE_FOLDER
# from flask import request, send_file, Blueprint
# from werkzeug.utils import secure_filename
# import os

# blueprint = Blueprint('file', __name__)


# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# def upload_file(file_id):
#     if 'file' not in request.files:
#         return False, "No file part"
#     file = request.files['file']
#     if file.filename == '':
#         return False, "No selected file"
#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         save_name = f"{file_id}-{filename}"
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], save_name))
#         return True, save_name


# @blueprint.route('/<string:file_name>', methods=['GET'])
# def download_file(file_name):
#     if '/' in file_name:
#         return 'error', 400
#     if file_name:
#         return send_file(f"{FILE_FOLDER}/{file_name}", attachment_filename='file.jpg')
#     return 'error', 400


# Option Two

# from flask import Flask

# UPLOAD_FOLDER = 'C:/uploads'

# app = Flask(__name__)
# #app.secret_key = "secret key"
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024




# import os
# import urllib.request
# from app import app
# from flask import Flask, request, redirect, jsonify
# from werkzeug.utils import secure_filename

# ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# def allowed_file(filename):
# 	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/multiple-files-upload', methods=['POST'])
# def upload_file():
# 	# check if the post request has the file part
# 	if 'files[]' not in request.files:
# 		resp = jsonify({'message' : 'No file part in the request'})
# 		resp.status_code = 400
# 		return resp
	
# 	files = request.files.getlist('files[]')
	
# 	errors = {}
# 	success = False
	
# 	for file in files:		
# 		if file and allowed_file(file.filename):
# 			filename = secure_filename(file.filename)
# 			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
# 			success = True
# 		else:
# 			errors[file.filename] = 'File type is not allowed'
	
# 	if success and errors:
# 		errors['message'] = 'File(s) successfully uploaded'
# 		resp = jsonify(errors)
# 		resp.status_code = 500
# 		return resp
# 	if success:
# 		resp = jsonify({'message' : 'Files successfully uploaded'})
# 		resp.status_code = 201
# 		return resp
# 	else:
# 		resp = jsonify(errors)
# 		resp.status_code = 500
# 		return resp

# if __name__ == "__main__":
#     app.run()


# For single file

# import os
# import urllib.request
# from app import app
# from flask import Flask, request, redirect, jsonify
# from werkzeug.utils import secure_filename

# ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# def allowed_file(filename):
# 	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/file-upload', methods=['POST'])
# def upload_file():
# 	# check if the post request has the file part
# 	if 'file' not in request.files:
# 		resp = jsonify({'message' : 'No file part in the request'})
# 		resp.status_code = 400
# 		return resp
# 	file = request.files['file']
# 	if file.filename == '':
# 		resp = jsonify({'message' : 'No file selected for uploading'})
# 		resp.status_code = 400
# 		return resp
# 	if file and allowed_file(file.filename):
# 		filename = secure_filename(file.filename)
# 		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
# 		resp = jsonify({'message' : 'File successfully uploaded'})
# 		resp.status_code = 201
# 		return resp
# 	else:
# 		resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
# 		resp.status_code = 400
# 		return resp

# if __name__ == "__main__":
#     app.run()


    # from flask import Flask
    # from flask_restful import Resource, Api, reqparse
    # import werkzeug

    # class UploadAudio(Resource):
    #   def post(self):
    #     parse = reqparse.RequestParser()
    #     parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
    #     args = parse.parse_args()
    #     audioFile = args['file']
    #     audioFile.save("your_file_name.jpg")