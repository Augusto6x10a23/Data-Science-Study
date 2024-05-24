from sklearn import tree

#[Speed, Weight(Ton)]
Speed = [[340, 2.34], [220, 1.78], [400, 2.89], [200, 1.25], [320, 2.47],
          [360, 2.03], [240, 1.96], [300, 2.65], [380, 2.13], [260, 1.55], [280, 2.71]]

Car = ["Italian", "German", "Swedish", "German", "Italian", "Italian",
       "German", "Italian", "Italian", "German", "German"]

clf = tree.DecisionTreeClassifier()

clf = clf.fit(Speed, Car)

prediction = clf.predict([[275, 1]])

print(prediction)
