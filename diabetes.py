#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 22:57:36 2021

@author: sarthakdallakoti
"""
import csv
import matplotlib.pyplot as plt

def generate_summary_for_web(csvfile, html_title, html_filename, show_barchart_gender=True):
    t_array = []
    groups = {}
    with open(csvfile, "r") as file:
        read = csv.reader(file)
        for rows in read:
            t_array.append(rows)

        for x in range(2,len(t_array[0]) - 1):                
            groups[t_array[0][x]] = {'Positive': {"Yes" : 0, "No" : 0}, 'Negative': {"Yes" : 0, "No" : 0}}

        for y in range(1, len(t_array)):
            for z in range(2,len(t_array[y]) - 1):
                if t_array[y][z] == "No" and t_array[y][len(t_array[y]) - 1] == 'Negative':
                    groups[t_array[0][z]]['Negative']["No"] = groups[t_array[0][z]]['Negative']["No"] + 1
                elif t_array[y][z] == "No" and t_array[y][len(t_array[y]) - 1] == 'Positive':
                    groups[t_array[0][z]]['Positive']["No"] = groups[t_array[0][z]]['Positive']["No"] + 1
                elif t_array[y][z] == "Yes" and t_array[y][len(t_array[y]) - 1] == 'Positive':
                    groups[t_array[0][z]]['Positive']["Yes"] = groups[t_array[0][z]]['Positive']["Yes"] + 1
                elif t_array[y][z] == "Yes" and t_array[y][len(t_array[y]) - 1] == 'Negative':
                    groups[t_array[0][z]]['Negative']["Yes"] = groups[t_array[0][z]]['Negative']["Yes"] + 1
    
    if show_barchart_gender:
        graph = [[0,0],[0,0]]

        for y in range(1, len(t_array)):
            if t_array[y][len(t_array[y]) - 1] == "Positive" and t_array[y][1] == "Male":
                graph[0][0] = graph[0][0] + 1
            elif t_array[y][len(t_array[y]) - 1] == "Positive" and t_array[y][1] == "Female":
                graph[0][1] = graph[0][1] + 1
            elif t_array[y][len(t_array[y]) - 1] == "Negative" and t_array[y][1] == "Male":
                graph[1][0] = graph[1][0] + 1
            elif t_array[y][len(t_array[y]) - 1] == "Negative" and t_array[y][1] == "Female":
                graph[1][1] = graph[1][1] + 1
    
        fig_size = plt.figure(figsize=(7,7))
        brac1 = [0,1]
        brac2 = [x + 0.125 for x in brac1]
        plt.bar(brac1, graph[0], color="maroon", width = 0.15, align= 'edge', label ='Male')
        plt.bar(brac2, graph[1], color="#ffa781", width = 0.15, align= 'edge', label ='Female')
        plt.title('Gender of Positive vs Negative Case', fontweight = 'bold', fontsize = 25, color= '#f49f1c')
        plt.xlabel("Class", fontweight ='bold', fontsize = 22)
        plt.ylabel("Value", fontweight ='bold', fontsize = 22)
        plt.xticks([r + 0.15 for r in range(len(brac2))],
        ['Positive', "Negative"])
        plt.legend()
        plt.savefig('barchart_gender.jpg')
        
        o_file = open(html_filename, 'w')
        o_file.write("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n\t<meta charset=\"UTF-8\">\n\t<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n\t<title>" + html_title+ "</title>\n</head>\n<body>\n\n")
        o_file.write("<table>\n<col>\n<colgroup span=\"8\"></colgroup>\n<tr>\n<th scope=\"col\">Attributes</th>\n<th colspan=\"4\" scope=\"colgroup\">Class</th>\n</tr>\n<tr>\n<th scope=\"col\"></th><th scope=\"colgroup\" colspan=\"2\">Positive</th><th scope=\"colgroup\" colspan=\"2\">Negative</th></tr><tr><th scope=\"col\"></th><th scope=\"colgroup\" colspan=\"1\">Yes</th><th scope=\"colgroup\" colspan=\"1\">No</th><th scope=\"colgroup\" colspan=\"1\">Yes</th><th scope=\"colgroup\" colspan=\"1\">No</th></tr>\n")
        
        for item in groups.items():
            o_file.write("<tr> <td>"+ item[0] +"</td>"+ "<td>" + str(item[1]["Positive"]["Yes"]) + "</td>" + "<td>" + str(item[1]["Positive"]["No"]) + "</td>" + "<td>" + str(item[1]["Negative"]["Yes"]) + "</td>" + "<td>" + str(item[1]["Negative"]["No"]) + "</td>" + "</tr>")
        o_file.write("</table>\n\n")
        o_file.write("<img src=\""+ "barchart_gender.jpg\"" + " alt=\"Gender of Positive vs Negative Case\">\n")
        o_file.write("\n</body>\n</html>")
        o_file.close()
    else:
        o_file = open(html_filename, 'w')
        o_file.write("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n\t<meta charset=\"UTF-8\">\n\t<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n\t<title>" + html_title+ "</title>\n</head>\n<body>\n\n")
        o_file.write("<table>\n<col>\n<colgroup span=\"8\"></colgroup>\n<tr>\n<th scope=\"col\">Attributes</th>\n<th colspan=\"4\" scope=\"colgroup\">Class</th>\n</tr>\n<tr>\n<th scope=\"col\"></th><th scope=\"colgroup\" colspan=\"2\">Positive</th><th scope=\"colgroup\" colspan=\"2\">Negative</th></tr><tr><th scope=\"col\"></th><th scope=\"colgroup\" colspan=\"1\">Yes</th><th scope=\"colgroup\" colspan=\"1\">No</th><th scope=\"colgroup\" colspan=\"1\">Yes</th><th scope=\"colgroup\" colspan=\"1\">No</th></tr>\n")
        
        for item in groups.items():
            o_file.write("<tr> <td>"+ item[0] +"</td>"+ "<td>" + str(item[1]["Positive"]["Yes"]) + "</td>" + "<td>" + str(item[1]["Positive"]["No"]) + "</td>" + "<td>" + str(item[1]["Negative"]["Yes"]) + "</td>" + "<td>" + str(item[1]["Negative"]["No"]) + "</td>" + "</tr>")
        o_file.write("</table>\n</body>\n</html>")
        o_file.close()
        
        
        
        
        
        