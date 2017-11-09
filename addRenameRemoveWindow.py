#==========================================
#      add rename remove
#==========================================
import maya.cmds as mc
if mc.window("add rename remove", exists =True):
    mc.deleteUI("add rename remove")
          
myWindow = mc.window("add rename remove", t="Add rename remove")
mc.columnLayout(adj = True)
mc.text(label = "Add above and Rename in Heirachy")
additionType = mc.optionMenuGrp(label = 'Type')
mc.menuItem(label = 'Group')
mc.menuItem(label = 'Joint')
mc.menuItem(label = 'Locator')
groupMe = mc.textFieldGrp(label = "Add above...", editable = True)
mc.text(label = "If left blank, your item will display as [name]_[typeEXT]")
renameMe = mc.textFieldGrp(label = "New Name", editable = True)
mc.button(label = "Execute", command = "combinefunc()")
mc.separator(height = 10, style = 'double')
mc.text(label = "Remove from Heirachy")
removeMe = mc.textFieldGrp(label = "Name", editable = True)
mc.button(label = "Execute", command = "removeTool()")
mc.showWindow(myWindow)

#==========================================
#      Defining functions
#==========================================
#      combinefunc
def combinefunc():
    selectAddition()
    renameGroup()

#++++++++++++++++++++++++++++++++++++++++++
#      add group
def addGroupTool():      
    jnt = mc.textFieldGrp(groupMe, query = True, text = True)
    
    parents = mc.listRelatives(jnt, p = True)
    print parents
    
    target = mc.group(empty = True)
   
    pc = mc.pointConstraint(jnt, target)
    mc.delete(pc)

    oc = mc.orientConstraint(jnt, target)
    mc.delete(oc)
    
    mc.parent(jnt, target)
    mc.parent(target, parents)

#++++++++++++++++++++++++++++++++++++++++++
#      add joint 
def addJointTool():      
    jnt = mc.textFieldGrp(groupMe, query = True, text = True)
    
    parents = mc.listRelatives(jnt, p = True)
    print parents
    
    target = mc.createNode("joint")
   
    pc = mc.pointConstraint(jnt, target)
    mc.delete(pc)

    oc = mc.orientConstraint(jnt, target)
    mc.delete(oc)
    
    mc.parent(target, parents)
    mc.parent(jnt, target)
    
    added = mc.select(target)
    
    return added

#++++++++++++++++++++++++++++++++++++++++++
#      add locator
def addLocatorTool():      
    jnt = mc.textFieldGrp(groupMe, query = True, text = True)
    
    parents = mc.listRelatives(jnt, p = True)
    print parents
    
    target = mc.spaceLocator(p = (0, 0, 0))
   
    pc = mc.pointConstraint(jnt, target)
    mc.delete(pc)

    oc = mc.orientConstraint(jnt, target)
    mc.delete(oc)
    
    mc.parent(jnt, target)
    mc.parent(target, parents)

#++++++++++++++++++++++++++++++++++++++++++
#      rename group
def renameGroup():
    toAdd = mc.optionMenuGrp(additionType, query = True, value = True)
    newName = mc.textFieldGrp(renameMe, query = True, text = True)
    itemName = mc.textFieldGrp(groupMe, query = True, text = True)
    if toAdd == "Group" and newName == "":
        groupName = mc.rename(itemName + "_GRP")    
        return groupName
    elif toAdd == "Joint" and newName == "":
        jointName = mc.rename(itemName + "_JNT")
        return jointName
    elif toAdd == "Locator" and newName == "":
        locatorName = mc.rename(itemName + "_LOC")
        return locatorName
    else:
        elseName = mc.rename(newName)
        return elseName

#++++++++++++++++++++++++++++++++++++++++++
#      remove tool        
def removeTool():
    toGo = mc.textFieldGrp(removeMe, query = True, text = True)
    
    parents = mc.listRelatives(toGo, p = True)
    print parents
    
    child = mc.listRelatives(toGo, c = True)
    print child
    
    mc.parent(child, parents)
    mc.delete(toGo)

#++++++++++++++++++++++++++++++++++++++++++
#      select addition
def selectAddition():
    toAdd = mc.optionMenuGrp(additionType, query = True, value = True)
    if toAdd == "Group":
        addGroupTool()
    elif toAdd == "Joint":
        addJointTool()
    elif toAdd == "Locator":
        addLocatorTool()