cd /tmp

git clone https://github.com/pypa/virtualenv.git

python virtualenv/virtualenv.py ~/Envs/pythonenv

source ~/Envs/pythonenv/bin/activate

pip install -r requirements.txt

python plot_wadj.py sample.graph sample.dot

dot -Tpng sample.dot -o sample.png
