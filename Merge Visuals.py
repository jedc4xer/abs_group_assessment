#filtered values 
workingDF = workingDF[workingDF['firmpdemp'] != 0]
workingDF = workingDF[workingDF['yibszfi_label'] == 'All firms']
workingDF = workingDF[workingDF['race_group_label'] == 'Total']

workingDF = workingDF[workingDF['industry'] != 'Industries not classified']

#Drop columns
workingDF.drop(['geo_id', 'name', 'industry_code', 'race_group_label', 'yibszfi_label'], axis = 1, inplace = True)

workingDF = workingDF[workingDF['gender'] != 'Total']
workingDF = workingDF[workingDF['industry'] != 'Total for all sectors']


#Visual 1: Number of Responses to Question by Business owner
df_bus_own = df_collection[2]
df_bus_own[df_bus_own['industry']!='Total for all sectors']
df_bus_own = df_bus_own[df_bus_own['gender']!='All owners of respondent firms']
x = df_bus_own[['qdesc_label','gender','geo_id']].groupby(['qdesc_label','gender']).count()
x = x.reset_index()
x.columns = ['qdesc_label', 'gender', 'count']

plt.figure(figsize=(20, 10))

ax = sns.barplot(data = x, x = 'qdesc_label', y = 'count', hue = 'gender',palette = 'Oranges')
ax.set(xlabel ="Question Codes", ylabel = "number of reponses", title ='Number of Responses to Question by Business owner')
plt.legend(title = "Gender", fontsize = 'large', title_fontsize = 20, loc = 2, bbox_to_anchor = (1,1))
plt.xticks(rotation = 70)
plt.show()

#Visual 2: Percentage of Business Owner Responses
x = x.groupby('qdesc_label')['count'].sum().reset_index()
plt.figure(figsize=(20, 10))
plt.pie(x['count'], labels=x['qdesc_label'], autopct='%1.0f%%', pctdistance = 1.1, labeldistance = 1.2)
plt.legend(title = "", fontsize = 'medium', title_fontsize = 10, loc = 3, bbox_to_anchor = (2,0))
plt.title('Percentage of Business Owner Responses')
plt.show()

#Visual 3: Number of Business Owner by Race
x = df_bus_own[['owner_race_label','gender','geo_id']].groupby(['owner_race_label','gender']).count().reset_index()

plt.figure(figsize=(20, 10))

sns.set(font_scale=2)

ax = sns.barplot(data = x, x = 'owner_race_label', y = 'geo_id', hue = 'gender', palette = 'Oranges')
ax.set_xlabel("Race of Business Owner", fontsize = 30)
ax.set_ylabel("Number of Business Owner", fontsize = 30)
ax.set_title("Number of Business Owner by Race", fontsize = 40)

plt.legend(title = "Gender", fontsize = 'large', title_fontsize = 20, loc = 2, bbox_to_anchor = (1,1))

plt.xticks(rotation = 70)
plt.show()
