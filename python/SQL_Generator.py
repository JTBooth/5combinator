__author__ = 'rbooth'

import Tkinter

root = Tkinter.Tk()

nameLabel = Tkinter.Label(root, text="Spell Name:")
nameString = Tkinter.StringVar()
nameEntry = Tkinter.Entry(root, textvariable=nameString)
nameLabel.grid(column=0, row=0)
nameEntry.grid(column=1, row=0)

levelLabel = Tkinter.Label(root, text="Spell Level:")
levelString = Tkinter.StringVar()
levelEntry = Tkinter.Entry(root, textvariable=levelString)
levelLabel.grid(column=0, row=1)
levelEntry.grid(column=1, row=1)

schoolLabel = Tkinter.Label(root, text="School:")
schoolString = Tkinter.StringVar()
schoolEntry = Tkinter.Entry(root, textvariable=schoolString)
schoolLabel.grid(column=0, row=2)
schoolEntry.grid(column=1, row=2)

castingTimeLabel = Tkinter.Label(root, text="Casting Time:")
castingTimeString = Tkinter.StringVar()
castingTimeEntry = Tkinter.Entry(root, textvariable=castingTimeString)
castingTimeLabel.grid(column=2, row=0)
castingTimeEntry.grid(column=3, row=0)

durationLabel = Tkinter.Label(root, text="Duration:")
durationString = Tkinter.StringVar()
durationEntry = Tkinter.Entry(root, textvariable=durationString)
durationLabel.grid(column=2, row=1)
durationEntry.grid(column=3, row=1)

rangeLabel = Tkinter.Label(root, text="Range")
rangeString = Tkinter.StringVar()
rangeEntry = Tkinter.Entry(root, textvariable=rangeString)
rangeLabel.grid(column=2, row=2)
rangeEntry.grid(column=3, row=2)

checkboxFrame = Tkinter.Frame(root)
checkboxFrame.grid(row=3, column=0, columnspan=4)

atHigherLevelsLabel = Tkinter.Label(checkboxFrame, text="Higher Level Version?")
atHigherLevelsBool = Tkinter.IntVar()
atHigherLevelsCheck = Tkinter.Checkbutton(checkboxFrame, variable=atHigherLevelsBool)
atHigherLevelsLabel.grid(row=0, column=0)
atHigherLevelsCheck.grid(row=1, column=0)

ritualLabel = Tkinter.Label(checkboxFrame, text="Available as Ritual?")
ritualBool = Tkinter.IntVar()
ritualCheck = Tkinter.Checkbutton(checkboxFrame, variable=ritualBool)
ritualLabel.grid(row=0, column=1)
ritualCheck.grid(row=1, column=1)

concentrationLabel = Tkinter.Label(checkboxFrame, text="Requires Concentration?")
concentrationBool = Tkinter.IntVar()
concentrationCheck = Tkinter.Checkbutton(checkboxFrame, variable=concentrationBool)
concentrationLabel.grid(row=0, column=2)
concentrationCheck.grid(row=1, column=2)

damagingLabel = Tkinter.Label(checkboxFrame, text="Deals Damage?")
damagingBool = Tkinter.IntVar()
damagingCheck = Tkinter.Checkbutton(checkboxFrame, variable=damagingBool)
damagingLabel.grid(row=0, column=3)
damagingCheck.grid(row=1, column=3)

complicatedLabel = Tkinter.Label(checkboxFrame, text="Is Complicated?")
complicatedBool = Tkinter.IntVar()
complicatedCheck = Tkinter.Checkbutton(checkboxFrame, variable=complicatedBool)
complicatedLabel.grid(row=0, column=4)
complicatedCheck.grid(row=1, column=4)

descriptionLabel = Tkinter.Label(root, text="Paste description here:")
descriptionText = Tkinter.Text(root, borderwidth=4, relief=Tkinter.SUNKEN)
descriptionLabel.grid(row=4, columnspan=2)
descriptionText.grid(row=5, columnspan=4)

outputLabel = Tkinter.Label(root, text="Your SQL command appears here:")
outputString = Tkinter.StringVar()
outputEntry = Tkinter.Entry(root, width=70, textvariable=outputString)
outputLabel.grid(row=6, columnspan=2)
outputEntry.grid(row=7, columnspan=4)

def produceOutput():
    textWithoutNewLines = descriptionText.get(1.0, Tkinter.END).replace("\n", " ")
    response = "INSERT INTO \"SPELLS\" VALUES("
    response += "\"" + nameString.get() + "\", "
    response += "\"" + levelString.get() + "\", "
    response += "\"" + schoolString.get() + "\", "
    response += "\"" + castingTimeString.get() + "\", "
    response += "\"" + durationString.get() + "\", "
    response += "\"" + rangeString.get() + "\", "
    response += "\"" + textWithoutNewLines + "\", "
    response += str(atHigherLevelsBool.get()) + ", "
    response += str(ritualBool.get()) + ", "
    response += str(concentrationBool.get()) + ", "
    response += str(damagingBool.get()) + ", "
    response += str(complicatedBool.get()) + ");"
    outputString.set(response)

outputButton = Tkinter.Button(root, text="Produce SQL command", command=produceOutput)
outputButton.grid(row=6, column=2)

root.mainloop()
