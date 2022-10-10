# Python_Intermediate


# 1. Create a diabetes.py module (30 marks)

Create a module called diabetes.py. In the module, create a function called generate_summary_for_web(csvfile, html_title, html_filename, show_barchart_gender=True) thatreadsspecificcsvfilesrelatedtodiabetes. These csv files will have the same column header, same number of columns, and in the same order. All columns in the csv files are attributes except the last column which is the class, either Positive of Negative.
The csvfile is the full name with extension of the csv file to be used (e.g., “diabetes_data.csv”). The html_title is a string for the title (<title> tag) of the html file specified by html_filename (e.g., “summary.html”). You can also use the same html_title as the <h1> heading at the beginning of the html page.
When this function is called with relevant parameters, the following will be produced:

A) An html file with the specified html_filename and html_title, with an html table on the total count for each value (Yes or No) of the attributes (except Age and Gender) 

B) If the value for the parameter show_barchart_gender is True, then a vertical bar chart showing the count for Positive and Negative cases for each Gender will be shown after the html table. Hint: You need to write codes (possibly in separate function) to plot the bar chart with pyplot in matplotlib and save the plot to current directory (refer savefig() method in pyplot), and display it on the html page. If the value for the parameter show_barchart_gender is False, the bar chart will not be created and displayed. 




#2. Lights out Puzzle (JavaScript)

