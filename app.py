from flask import Flask, request, render_template_string, send_file
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>GlowEdit Pro</title>
<style>
body { background:#0a0a0a; color:white; font-family:Arial; text-align:center; padding:40px; }
.box { background:#1a1a1a; padding:30px; border-radius:20px; max-width:500px; margin:0 auto; }
button { background:#ff2e93; color:white; border:none; padding:15px 30px; border-radius:30px; font-size:18px; cursor:pointer; width:100%; }
input { margin:20px 0; }
</style>
</head>
<body>
<div class="box">
<h1>GlowEdit ✨</h1>
<p>Pro Background Remover - HD</p>
<form method="POST" enctype="multipart/form-data">
<input type="file" name="image" required><br>
<button type="submit">Remove Background</button>
</form>
</div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        input_img = Image.open(file.stream)
        output_img = remove(input_img)
        img_io = io.BytesIO()
        output_img.save(img_io, 'PNG')
        img_io.seek(0)
        return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='glowedit_hd.png')
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)