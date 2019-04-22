from flask import Flask,render_template, request
from find_stock_sharpe_by_yahoo_fin import find_stock_sharpe_by_yahoo_fin
from stock import Stock

app = Flask(__name__)

@app.route("/")
def index():
	name="Sam"
	age=94
	return render_template('index.html', name=name, age=age)

@app.route("/stock_input", methods=['POST','GET'])
def stock_input():
	if request.method=='POST':
		code=request.form['code']
		return render_template('stock_detail.html', code=code)
	else:
		return render_template('stock_input.html')


@app.route("/stock_detail", methods=['POST','GET'])
def stock_detail():
	# sharpe=0.9
	myStock=find_stock_sharpe_by_yahoo_fin(request.form['code'])
	return render_template('stock_detail.html',
		code=myStock.code,
		stock_annualised_return= myStock.stock_annualised_return,
		stock_return_stdev=myStock.stock_return_stdev,
		stock_sharpe_ratio=myStock.stock_sharpe_ratio)

if __name__ == "__main__":
    app.run()