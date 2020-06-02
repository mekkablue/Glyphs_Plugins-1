# encoding: utf-8
###########################################################################################################
#Read the docs: https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/General%20Plugin
###########################################################################################################

from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *
import vanilla


#global variables
Active_Font = ""








############################################### File Handling ###############################################
#--------------------------------------------
#Get the active font to work with
def resetCache(debug):
    for font in Glyphs.fonts:
        if not font.familyName.startswith("Working draft of"):
            if not font.familyName.startswith("The horizontal black mass distribution of"):
                if not font.familyName.startswith("The rhythm of"):
                    if not font.familyName.startswith("Extracted master from"):
                        if debug:print("\nResetting cache: the active font will be: %s"%font)
                        Active_Font = font
                        return Active_Font
    return False

#--------------------------------------------
#Create a duplicate file
def CreateWorkingFile(Active_Font):
    InvisibleWorkingFile = Active_Font.copy()
    InvisibleWorkingFile.familyName = "Working draft of %s"%InvisibleWorkingFile.familyName
    #Erase all glyphs in the copied font
    for thisGlyph in InvisibleWorkingFile.glyphs:
        for thisLayer in thisGlyph.layers:
            thisLayer.decomposeComponents()
            thisLayer.removeOverlap()
            for hint in reversed( range( len(thisLayer.hints) )):
                del thisLayer.hints[hint]
            
    return InvisibleWorkingFile


#--------------------------------------------
#Create a duplicate file
def CreateGraphFile(Active_Font):
    FileForDistribution = Active_Font.copy()
    FileForDistribution.familyName = "The horizontal black mass distribution of %s" %Active_Font.familyName
    #Erase all glyphs in the copied font
    FileForDistribution.disableUpdateInterface()
    for thisGlyph in FileForDistribution.glyphs:
        thisGlyph.leftMetricsKey = ""
        thisGlyph.rightMetricsKey = ""
        thisGlyph.widthMetricsKey = ""
        for thisLayer in thisGlyph.layers:
            thisLayer.leftMetricsKey = ""
            thisLayer.rightMetricsKey = ""
            thisLayer.widthMetricsKey = ""
            for x in range(len(thisLayer.components))[::-1]:
                del(thisLayer.components[x])
            for x in range(len(thisLayer.background.components))[::-1]:
                del(thisLayer.background.components[x])
            for thisPath in range(len(thisLayer.paths))[::-1]:
                del thisLayer.paths[thisPath]
            for thisPath in range(len(thisLayer.background.paths))[::-1]:
                del thisLayer.background.paths[thisPath]
            for hint in reversed( range( len(thisLayer.hints) )):
                del thisLayer.hints[hint]
            for anchor in thisLayer.anchors:
                del thisLayer.anchors[anchor.name]
    FileForDistribution.enableUpdateInterface()
    return FileForDistribution


#--------------------------------------------
#Create a duplicate file
def CreateRhythmFile(Active_Font):
    FileForRhythm = Active_Font.copy()
    FileForRhythm.familyName = "The rhythm of %s" %Active_Font.familyName
    #Erase all glyphs in the copied font
    FileForRhythm.disableUpdateInterface()
    for thisGlyph in FileForRhythm.glyphs:
        thisGlyph.leftMetricsKey = ""
        thisGlyph.rightMetricsKey = ""
        thisGlyph.widthMetricsKey = ""
        for thisLayer in thisGlyph.layers:
            thisLayer.leftMetricsKey = ""
            thisLayer.rightMetricsKey = ""
            thisLayer.widthMetricsKey = ""
            for x in range(len(thisLayer.components))[::-1]:
                del(thisLayer.components[x])
            for x in range(len(thisLayer.background.components))[::-1]:
                del(thisLayer.background.components[x])
            for thisPath in range(len(thisLayer.paths))[::-1]:
                del thisLayer.paths[thisPath]
            for thisPath in range(len(thisLayer.background.paths))[::-1]:
                del thisLayer.background.paths[thisPath]
            for hint in reversed( range( len(thisLayer.hints) )):
                del thisLayer.hints[hint]
            for anchor in thisLayer.anchors:
                del thisLayer.anchors[anchor.name]
    FileForRhythm.enableUpdateInterface()
    return FileForRhythm


#--------------------------------------------
#Create a duplicate file
def CreateScaledFile(Active_Font):
    #This function is based on Maarten Renckens' script 'Extract Master'
    FileForScaling = Active_Font.copy()
    FileForScaling.familyName = "Extracted master from %s" %Active_Font.familyName
    #Erase all other masters in the copied font
    FileForScaling.disableUpdateInterface()
    
    #Delete masters
    toKeep = FileForScaling.masters[0].id
    numberOfMasters = len(FileForScaling.masters)
    for i in range( numberOfMasters )[::-1]:
        if FileForScaling.masters[i].id != toKeep:
            del FileForScaling.masters[i]
    #Delete all Layers in the remaining Master (this is based on Mekkablue's script)
    searchTerms = [ "[]", "{}" ]
    for thisGlyph in FileForScaling.glyphs:
        thisGlyph.beginUndo()
        numberOfLayers = len( thisGlyph.layers )
        thisGlyphName = thisGlyph.name

        if str(thisGlyphName)[:7] != "_smart.":
            for i in range( numberOfLayers )[::-1]:
                thisLayer = thisGlyph.layers[i]
                if thisLayer.layerId != thisLayer.associatedMasterId: # not the master layer
                    thisLayerName = thisLayer.name
                    thisLayerShouldBeRemoved = True
                    if thisLayerName: # always delete unnamed layers
                        for parentheses in searchTerms:
                            opening = parentheses[0]
                            closing = parentheses[1]
                            
                            # check if ONE of them is at the END of the layer name, like:
                            # Bold [160], Bold [160[, Bold ]160], Regular {120}
                            if thisLayerName.endswith(opening) or thisLayerName.endswith(closing):
                                thisLayerShouldBeRemoved = False
                                
                    if thisLayerShouldBeRemoved:
                        del thisGlyph.layers[i]
        #And delete all other elements from the glyph

        #thisGlyph.leftMetricsKey = "" #DON'T, because of compatibility issues.
        #thisGlyph.rightMetricsKey = ""
        #thisGlyph.widthMetricsKey = ""
        for thisLayer in thisGlyph.layers:
            #thisLayer.leftMetricsKey = ""
            #thisLayer.rightMetricsKey = ""
            #thisLayer.widthMetricsKey = ""
            for x in range(len(thisLayer.components))[::-1]:
                del(thisLayer.components[x])
            for x in range(len(thisLayer.background.components))[::-1]:
                del(thisLayer.background.components[x])
            for thisPath in range(len(thisLayer.paths))[::-1]:
                del thisLayer.paths[thisPath]
            for thisPath in range(len(thisLayer.background.paths))[::-1]:
                del thisLayer.background.paths[thisPath]
            for hint in reversed( range( len(thisLayer.hints) )):
                del thisLayer.hints[hint]
            for anchor in thisLayer.anchors:
                del thisLayer.anchors[anchor.name]
        thisGlyph.endUndo()
        
    FileForScaling.enableUpdateInterface()
    return FileForScaling

















#--------------------------------------------
#Get the stroke width of the letter 'i'
def getStrokeThicknessLowercase(debug, Active_Font):
    if debug:print("\n<<<Starting the function getStrokeThicknessLowercase")
    #Take the metrics and take half the x-height
    halfLowercaseHeight = Active_Font.masters[0].xHeight/2
    
    #Cut the 'i' at half the x-height
    intersectionLowercase =  Active_Font.glyphs["i"].layers[0].intersectionsBetweenPoints((-1000,halfLowercaseHeight),(Active_Font.glyphs["i"].layers[0].width+1000,halfLowercaseHeight), True)
    if len(intersectionLowercase) == 4:
        iStrokeThickness = intersectionLowercase[2].x - intersectionLowercase[1].x
        if debug:print("The detected thickness of the i is: %s units" %iStrokeThickness)
    else:
        if debug:print("The stroke width could not be determined for the lowercase: using a default value of 100.")
        Message("The stroke width could not be determined for the lowercase. Please check if the right font is active, or manually insert values. A reason could be that the letter 'i' is not drawn, or that the design is too complex. A default value will be used.", "Warning", OKButton=None)
        return 100 #provide some value to work with
    return iStrokeThickness


#--------------------------------------------
#Get the stroke width of the letter 'i'
def getStrokeThicknessUppercase(debug, Active_Font):
    if debug:print("\n<<<Starting the function getStrokeThicknessUppercase")
    #Take the metrics and take half the Capital height
    halfCapitalHeight = Active_Font.masters[0].capHeight/2
    
    #Cut the 'I' at half the Capital height
    intersectionUppercase =  Active_Font.glyphs["I"].layers[0].intersectionsBetweenPoints((-1000,halfCapitalHeight),(Active_Font.glyphs["I"].layers[0].width+1000,halfCapitalHeight), True)
    if len(intersectionUppercase) == 4:
        IStrokeThickness = intersectionUppercase[2].x - intersectionUppercase[1].x
        if debug:print("The detected thickness of the I is: %s units" %IStrokeThickness)
    else:
        #skipped_glyphs.append(glyph.name)
        if debug:print("The stroke width could not be determined for the uppercase: using a default value of 100.")
        Message("The stroke width could not be determined for the uppercase. Please check if the right font is active, or manually insert values. A reason could be that the letter 'I' is not drawn, or that the design is too complex. A default value will be used.", "Warning", OKButton=None)
        return 100 #provide some value to work with
    return IStrokeThickness



def detectStrokeThicknesses(debug, self, Active_Font):
    iStrokeThickness = 0
    IStrokeThickness = 0
    iStrokeThickness = getStrokeThicknessLowercase(debug, Active_Font)
    IStrokeThickness = getStrokeThicknessUppercase(debug, Active_Font)
    Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.AutoDetected_i"] = iStrokeThickness
    Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.AutoDetected_I"] = IStrokeThickness
    
    # Set values in the window
    self.UIAutoDetected_i.setStringValue_(iStrokeThickness)
    self.UIAutoDetected_I.setStringValue_(IStrokeThickness)
    return iStrokeThickness, IStrokeThickness





















############################################### Distribution ###############################################

#--------------------------------------------
#Analyse the letter for the black mass and enlist that
def DetermineBlackMass(debug, preciseness, thisLayer, InvisibleWorkingFile, FileForDistribution):
    if debug:print("\n<<<Starting the function DetermineBlackMass on the glyph '%s'" %thisLayer.parent.name)
    activeGlyphName = thisLayer.parent.name
    ActiveLayer = InvisibleWorkingFile.glyphs[activeGlyphName].layers[thisLayer.name]
    #Analyse the glyphs vertically per horizontally defined preciseness
    Xprogress = -1000#this value to start counting from before [0,0]
    #Prepare an empty path
    listOfIntersectionPointsXThisGlyph = []
    #remember in the analysis if a mass was detected, a glyphs can contain multiple shapes
    partOfEarlierDetectedMass = False

    ########Make a list of all intersections:
    while Xprogress <= ActiveLayer.width+1000:#count till way behind the glyphs width.
        #draw an intersection from bottom to top
        intersection = ActiveLayer.intersectionsBetweenPoints((Xprogress,-1500),(Xprogress,+2500), True)
        
        #only perform an action if a black mass was detected:
        if len(intersection) > 2:
            #If no previous mass was detected, create a starting point:
            if partOfEarlierDetectedMass == False:
                listOfIntersectionPointsXThisGlyph += [[Xprogress, 0]]
            #from this point on, make sure that it connects to the earlier black mass:
            partOfEarlierDetectedMass = True
            #prepare variables for annotating the black mass:
            totalHeightBlackMass=0
            CurrentIntersectionPoint=2#Start with the third intersection
            #for each two intersections, count the length of the intersection in the black mass. ##############in a triangle, it provides an error!
            while CurrentIntersectionPoint <= len(intersection)-2:
                #But only count if it effectively is a part of the letter: do not count counters,...
                if InvisibleWorkingFile.glyphs[activeGlyphName].layers[thisLayer.name].completeBezierPath.containsPoint_((Xprogress, float(intersection[CurrentIntersectionPoint-1].y)+0.03)):
                    totalHeightBlackMass += intersection[CurrentIntersectionPoint].y - intersection[CurrentIntersectionPoint-1].y
                CurrentIntersectionPoint+=1
            #add this value to the list, as part of the later graph:
            Node = [[Xprogress, totalHeightBlackMass]]
            listOfIntersectionPointsXThisGlyph += Node
        
        #if no intersection was found, it could mean that there are multiple shapes. Close the previous path.
        elif len(intersection) == 2:
            if partOfEarlierDetectedMass == True:
                Node = [[Xprogress-preciseness, 0]]
                listOfIntersectionPointsXThisGlyph += Node
                listOfIntersectionPointsXThisGlyph += ["CLOSE PATH"]
                partOfEarlierDetectedMass = False
        
        Xprogress += preciseness#till the width of the glyphs is analysed
    return listOfIntersectionPointsXThisGlyph


#--------------------------------------------
#Draw the black mass of the letter
def DrawBlackMass(debug, mass, thisLayer, InvisibleWorkingFile, FileForDistribution):
    activeGlyphName = thisLayer.parent.name
    if debug:print("\n<<<Starting the function DrawBlackMass for the glyph '%s'" %activeGlyphName)
    Path = GSPath()
    heightPosition = ""#To remember the previous y-height, in order to possibly skip unnecessary nodes
    
    #Analyse the incoming data
    for Data in mass:
        #Detect when to close paths, possibly drawing separate paths
        if Data == "CLOSE PATH":
            Path.closed = True
            Path.reverse()#otherwise it contains a white fill
            FileForDistribution.glyphs[activeGlyphName].layers[0].paths.append(Path)
            #reset info
            Path = GSPath()
            heightPosition = ""
        else:
            NodeToAdd = GSNode()
            NodeToAdd.position = (Data[0], Data[1])
            heightPosition = Data[1]
            Path.nodes.append(NodeToAdd)











############################################### Rhythm ###############################################

#--------------------------------------------
#determine the position of the rhythm
def calculateRhythm(debug, FileForDistribution, FileForRhythm, thisLayer, preciseness):
    if debug:print("\n<<<Starting the function calculateRhythm")
    activeGlyphName = thisLayer.parent.name
    ActiveLayer = FileForDistribution.glyphs[activeGlyphName].layers[thisLayer.name]
    buffermin = 0
    buffermax = 0
    desiredStrokeThickness = 0
    
    #provide a different desiredStrokeThickness for upper/lowercase, and
    if activeGlyphName[0].isupper():
        if Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.OverwriteDetected"] == 0:
            desiredStrokeThickness = Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.AutoDetected_I"]
        else:
            desiredStrokeThickness = Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.Manual_I"]
        
    else:
        if Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.OverwriteDetected"] == 0:
            desiredStrokeThickness = Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.AutoDetected_i"]
        else:
            desiredStrokeThickness = Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.Manual_i"]
    if debug:print("The desired stroke thicknesses is: %s" %(desiredStrokeThickness))
    
    Xprogress = -1000#this value to start counting from before [0,0]
    currentlyAnalysingMass = False
    wasFalling = False
    FirstXvalueToFindMass = 0
    encounteredPeaks = []
    lastLowestPeak = 0
    LastHighestPeak = 0
    LastValue = 0



    #Make a list of all intersections:
    #Memory hack!: first go through x-values and determine peak positions, as an analysis through y-values took too much memory
    
    #remember in the analysis if a mass was detected, a glyphs can contain multiple shapes:
    partOfEarlierDetectedMass = False
    
    #Make a list of all intersections:
    while Xprogress <= ActiveLayer.width+1000:#count till way behind the glyphs width.
        #draw an intersection from bottom to top
        intersection = ActiveLayer.intersectionsBetweenPoints((Xprogress,-1500),(Xprogress,+2500), True)
        #only perform an action if a black mass was detected:
        if len(intersection) > 2:
            #Set the begin for the current detection
            if currentlyAnalysingMass == False:
                currentlyAnalysingMass = True
                FirstXvalueToFindMass = Xprogress
            elif currentlyAnalysingMass == True:
                #Case: raising graph
                if intersection[len(intersection)-2].y >= LastValue and wasFalling == False:
                    #if debug:print("case1, %s"%LastValue)
                    LastValue = intersection[len(intersection)-2].y
                    LastHighestPeak = intersection[len(intersection)-2].y
                #Case: falling graph
                elif intersection[len(intersection)-2].y < LastValue:
                    #if debug:print("case2, %s"%LastValue)
                    LastValue = intersection[len(intersection)-2].y
                    wasFalling = True
                    lowestFalling = intersection[len(intersection)-2].y
                    latestFallingPoint = Xprogress
                #Case: raising graph, setting breakpoint after falling BUT ONLY if raising more than 15! to catch irregularities.
                elif intersection[len(intersection)-2].y >= LastValue and wasFalling == True:
                    #if debug:print("case3, %s"%LastValue)
                    LastValue = intersection[len(intersection)-2].y
                    #For going higher again with more than 15 units
                    if intersection[len(intersection)-2].y >= lowestFalling+15:
                        encounteredPeaks += [[FirstXvalueToFindMass, latestFallingPoint]]
                        FirstXvalueToFindMass = latestFallingPoint+preciseness
                        wasFalling = False
        #when no black mass is detected
        elif len(intersection) == 2:
            #but there was one previously
            if currentlyAnalysingMass == True:
                encounteredPeaks += [[FirstXvalueToFindMass, Xprogress-preciseness]]
            #reset all values, allowing to start over
            currentlyAnalysingMass = False
            wasFalling = False
            LastValue = 0
        Xprogress += preciseness#till the width of the glyphs is analysed
    if debug:print("High peaks in the graphs are situated between: %s"%encounteredPeaks)
    
    
    
    #Find the position of the rhythm
    #Prepare an empty path
    listOfRhythmPositions = []
    TresholdStrokeLength = Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.TresholdStrokeLength"]
    
    for nodes in encounteredPeaks:
        foundTheRhythm = False
        #Analyse the glyphs vertically per horizontally defined preciseness
        Yprogess = 2000#this value to start counting from high enough
        
        while Yprogess >= -1 and foundTheRhythm == False:#count till way behind the glyphs width. Start high, as there are the lowest points in the graphs
            #draw an intersection left to right
            intersection = ActiveLayer.intersectionsBetweenPoints((nodes[0],Yprogess),(nodes[1],Yprogess), True)
            #only perform an action if a black mass was detected:
            if len(intersection) > 2:
                #Detect if there is a black mass wider than the stroke thickness:
                item = 1
                while item < len(intersection)-2:
                    if float(intersection[item+1].x) - float(intersection[item].x) >= desiredStrokeThickness:
                        #And check if this is also part of the letter (thus black)
                        if ActiveLayer.completeBezierPath.containsPoint_((float(intersection[item].x)+0.03, Yprogess)):
                            #if this stroke is long enough, add this value to the list, as part of the later graph:
                            if Yprogess >= TresholdStrokeLength:
                                Node = [[float(intersection[item].x), float(intersection[item+1].x)]]
                                listOfRhythmPositions += Node
                            else:
                                if debug:print("A stroke was found, but it was too small: %s units" %Yprogess)
                            foundTheRhythm = True
                    item += 1
            Yprogess -= preciseness/2#Work more precise, to estimate the stroke width better. till the width of the glyphs is analysed
    
        
    #if a log is requested, print the data
    if debug:
        print("for the glyph '%s' was the following data found:" %activeGlyphName)
        for item in listOfRhythmPositions:
            print(item)
    return listOfRhythmPositions



#--------------------------------------------
#Create the rhythm
def DrawTheRhythm(debug, FileForDistribution, FileForRhythm, thisLayer, listOfRhythmPositions):
    if debug:print("\n<<<Starting the function DrawTheRhythm")
    activeGlyphName = thisLayer.parent.name
    ActiveLayer = FileForRhythm.glyphs[activeGlyphName].layers[thisLayer.name]
    
    ActiveLayer.background = thisLayer.copy()
    
    #check the height of the rhythm to draw:
    strokeHeight = 1000
    strokeBottom = 0
    if Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.DetectSerifs"]:
        strokeBottom = -500
        strokeHeight = FileForRhythm.masters[0].ascender + 300
    elif activeGlyphName[0].isupper():
        strokeHeight = FileForRhythm.masters[0].capHeight
    else:
        strokeHeight = FileForRhythm.masters[0].xHeight
        
    
    for nodes in listOfRhythmPositions:
        StrokeOfRhythm = GSPath()
        StrokeCoordinates = [
            [ nodes[0], strokeBottom ],
            [ nodes[1], strokeBottom ],
            [ nodes[1], strokeHeight ],
            [ nodes[0], strokeHeight ]
        ]
        
        for thisPoint in StrokeCoordinates:
            newNode = GSNode()
            newNode.type = GSLINE
            newNode.position = ( thisPoint[0], thisPoint[1] )
            StrokeOfRhythm.nodes.append( newNode )
        StrokeOfRhythm.closed = True
        
        ActiveLayer.paths.append(StrokeOfRhythm)
        ActiveLayer.width = thisLayer.width
        #The determined rectangle is placed in the previous function.
















############################################### Scale ###############################################
def getNewXPosition(debug, Active_Font, currentXValue, zonesNegative, zonesPositive, customScale):
    if debug:print("\n<<<Starting the function getNewXPosition")
    
    newXValue = 0
    lastPassedZone = 0
    newXValueFound = False
    currentList = [] #the zonesNegative or zonesPositive to work with
    #for negative nodes
    if currentXValue <0:
        currentList = zonesNegative
        for zone in currentList:
            #block the iteration when the new newXValue is already found
            if newXValueFound == False:
                if zone[0] <= currentXValue:
                    if newXValue != 0:
                        newXValue += (currentXValue + lastPassedZone) * zone[1]
                    elif newXValue == 0: #if the node is close to zero and fits within one zone.
                        newXValue += currentXValue * zone[1]
                    newXValueFound = True
                    
                elif zone[0] > currentXValue:
                    newXValue += (zone[0] - lastPassedZone) * zone[1]
                    lastPassedZone = zone[0]
            #print("newXValueFound: %s, currentXValue: %s, zone[0]: %s, zone[1]: %s, lastPassedZone: %s, newXValue: %s" %(newXValueFound, currentXValue, zone[0], zone[1], lastPassedZone, newXValue))
        #anchors can go outside the SB. This catches those anchors.
        if newXValueFound == False:
            newXValue += (currentXValue - lastPassedZone) * customScale
            print("too large")
    #for positive nodes
    elif currentXValue >0:
        currentList = zonesPositive
        for zone in currentList:
            #block the iteration when the new newXValue is already found
            if newXValueFound == False:
                if zone[0] >= currentXValue:
                    if newXValue != 0:
                        newXValue += (currentXValue - lastPassedZone) * zone[1]
                    elif newXValue == 0: #if the node is close to zero and fits within one zone.
                        newXValue += currentXValue * zone[1]
                    newXValueFound = True
                    
                elif zone[0] < currentXValue:
                    newXValue += (zone[0] - lastPassedZone) * zone[1]
                    lastPassedZone = zone[0]
            #print("newXValueFound: %s, currentXValue: %s, zone[0]: %s, zone[1]: %s, lastPassedZone: %s, newXValue: %s" %(newXValueFound, currentXValue, zone[0], zone[1], lastPassedZone, newXValue))
        #anchors can go outside the SB. This catches those anchors.
        if newXValueFound == False:
            newXValue += (currentXValue - lastPassedZone) * customScale
            print("too large")
    if debug:print("moved X from X=%s to X=%s:" %(currentXValue, newXValue))
    return newXValue





def scaling(debug, Active_Font, FileForScaling, listOfRhythmPositions, thisLayer):
    #!!!!!! to add: something for empty glyphs
    if debug:print("\n<<<Starting the function scaling")
    activeGlyphName = thisLayer.parent.name
    FileForScaling.glyphs[activeGlyphName].layers[0] = thisLayer.copy()
    ActiveLayer = FileForScaling.glyphs[activeGlyphName].layers[0]#!!!!!!! Use zero to call the layer, or the id, but not a name!
    
    
    customScale = float(Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.ScaleRest"])/100
    customStrokeScale = float(Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.ScaleThickness"])/100
    customSideBearingsScale = float(Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.ScaleSideBearings"])/100
    RhythmExtension = float(Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.ExtendStrokeWidth"])
    #remember some data for later
    existingLSB = ActiveLayer.LSB
    existingRSB = ActiveLayer.RSB
    #Create the different zones within the letter #This will be a list [[X,Z]], in which X is the horizontal coordinate and Z the scale for that distance
    zonesNegative = []
    zonesPositive = []
    #handle negative sidebearings
    if existingLSB < 0:
        #if the rhythm does not immediately start while there is a negative SB
        if existingLSB != listOfRhythmPositions[0][0]:
            zonesNegative += [[existingLSB, customScale]]
        #add all other negative zones
        for RhythmBoundary in listOfRhythmPositions:
            if RhythmBoundary[0] < 0:
                zonesNegative += [[RhythmBoundary[0], customStrokeScale]]
            if RhythmBoundary[1] < 0:
                zonesNegative += [[RhythmBoundary[1], customScale]]
        print(zonesNegative)
    #handle positive sidebearings
    elif existingLSB > 0 and existingLSB != 0:
        zonesPositive += [[existingLSB, customSideBearingsScale]]
    #handle all other positive zones
    for RhythmBoundary in listOfRhythmPositions:
        if RhythmBoundary[0] > 0:
            #it could be that the LSB ends at the rhythm, so some extra tests are necessary
            if zonesNegative != []:
                if RhythmBoundary[0] != (zonesNegative[len(zonesNegative)-1][0]):
                    zonesPositive += [[RhythmBoundary[0], customScale]]
            elif zonesPositive != []:
                if RhythmBoundary[0] != (zonesPositive[len(zonesPositive)-1][0]):
                    zonesPositive += [[RhythmBoundary[0], customScale]]
        if RhythmBoundary[1] > 0:
            zonesPositive += [[RhythmBoundary[1], customStrokeScale]]
    #Add the zone between the latest stroke and the RSB
    if (zonesPositive[len(zonesPositive)-1][0]) < (ActiveLayer.width - existingRSB):
        zonesPositive += [[(ActiveLayer.width-existingRSB), customScale]]
    zonesNegative.reverse() #reverse makes it easier to work with both lists in the same way later on
    #the RSB comes later, it does not need to be in the list.
    
    #re-position every x-value of nodes, anchors, and origins of components (scale)
    for thisPath in ActiveLayer.paths:
        for thisNode in thisPath.nodes:
            currentXValue = thisNode.x
            thisNode.x = getNewXPosition(debug, Active_Font, currentXValue, zonesNegative, zonesPositive, customScale)
    print(ActiveLayer.components)
    for component in ActiveLayer.components:
        print(component.position)
        currentXValue = component.position.x
        component.x = getNewXPosition(debug, Active_Font, currentXValue, zonesNegative, zonesPositive, customScale)
        print(component.position)
    for anchor in ActiveLayer.anchors:
        currentXValue = anchor.x
        anchor.x = getNewXPosition(debug, Active_Font, currentXValue, zonesNegative, zonesPositive, customScale)
    
    
    
    
    # + move the components/anchors
    #scale the strokes
    #scale the RSB. The LSB should already be ok by scaling the paths
    ActiveLayer.RSB = existingRSB * customSideBearingsScale
    ActiveLayer.parent.color = 5






























################################################# Main function #################################################
def main_steps(makeDistribution, makeRhythm, makeScale):
    debug = Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.ExportLog"]
    Active_Font = resetCache(debug)
    Glyphs.clearLog()
    #############################
    if Active_Font == False:
        Message("No useful file detected. Make sure the names of the files do not start with 'Working draft of', 'The horizontal black mass distribution of', 'The rhythm of' or 'Extracted master from'.")
    elif Active_Font.selectedLayers == None:
        Message("Please, first select the glyphs which should be analysed.")
    else:
        #reset the data
        InvisibleWorkingFile = ""
        FileForDistribution = ""
        FileForRhythm = ""
        FileForScaling = ""
        #set a higer grid for better details
        originalGridSubDivisions = Active_Font.gridSubDivisions#Backup for later
        Active_Font.gridSubDivisions = 100
        preciseness = float(Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.Preciseness"])
        
        ##################################
        ### Create the necessary files ###
        ##################################
        
        #create a working file that does not contain unnecessary details, nor overlap in paths
        InvisibleWorkingFile = CreateWorkingFile(Active_Font)
        #Check if new or merged files are required
        if Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.MergeFiles"] == 0:
            #ALWAYS create a file for the distribution of the black mass
            FileForDistribution = ""
            FileForDistribution = CreateGraphFile(Active_Font)
            #But only show this file if requested
            if makeDistribution:
                Glyphs.fonts.append(FileForDistribution)
            #create a file for the rhythm
            if makeRhythm or makeScale:
                FileForRhythm = ""
                FileForRhythm = CreateRhythmFile(Active_Font)
                if makeRhythm:
                    Glyphs.fonts.append(FileForRhythm)
            #create a file for the variations
            if makeScale:
                FileForScaling = ""
                FileForScaling = CreateScaledFile(Active_Font)
                Glyphs.fonts.append(FileForScaling)
                FileForScaling.gridSubDivisions = originalGridSubDivisions
        else:
            #ALWAYS create a file for the distribution of the black mass
            exists = False
            for font in Glyphs.fonts:
                if font.familyName.startswith("The horizontal black mass distribution"):
                    FileForDistribution = font
                    exists = True
                    if debug:print("Files will be merged")
            if exists == False:
                FileForDistribution = CreateGraphFile(Active_Font)
                if makeDistribution:
                    Glyphs.fonts.append(FileForDistribution)
            #create a file for the rhythm
            if makeRhythm or makeScale:
                exists = False
                for font in Glyphs.fonts:
                    if font.familyName.startswith("The rhythm of"):
                        FileForRhythm = font
                        exists = True
                        if debug:print("Files will be merged")
                if exists == False:
                    FileForRhythm = CreateRhythmFile(Active_Font)
                    if makeRhythm:
                        Glyphs.fonts.append(FileForRhythm)
            #create a file for the variations
            if makeScale:
                exists = False
                for font in Glyphs.fonts:
                    if font.familyName.startswith("Extracted master from"):
                        FileForScaling = font
                        exists = True
                        if debug:print("Files will be merged")
                if exists == False:
                    FileForScaling = CreateScaledFile(Active_Font)
                    Glyphs.fonts.append(FileForScaling)
                    FileForScaling.gridSubDivisions = originalGridSubDivisions
        
        ##################################
        ###          Analyse and draw       ###
        ##################################
        
        for thisLayer in Active_Font.selectedLayers:
            Glyphs.clearLog()
            #always analyze the black mass
            mass = DetermineBlackMass(debug, preciseness, thisLayer, InvisibleWorkingFile, FileForDistribution)
            DrawBlackMass(debug, mass, thisLayer, InvisibleWorkingFile, FileForDistribution)
            #Calculate where the rhythm is positioned
            if makeRhythm or makeScale:
                Glyphs.clearLog()
                listOfRhythmPositions = calculateRhythm(debug, FileForDistribution, FileForRhythm, thisLayer, preciseness)
                if makeRhythm:
                    DrawTheRhythm(debug, FileForDistribution, FileForRhythm, thisLayer, listOfRhythmPositions)
            if makeScale:
                Glyphs.clearLog()
                scaling(debug, Active_Font, FileForScaling, listOfRhythmPositions, thisLayer)
        
        #set the grid back to the default
        Active_Font.gridSubDivisions = originalGridSubDivisions






























class RhythmInfluencer(GeneralPlugin):
    
    #Everything to describe the plugin
    @objc.python_method
    def settings(self):
        #plugin name
        self.name = Glyphs.localize({'en': u'Rhythm Influencer'})
        
        
    #Everything on the Glyphsapp start
    @objc.python_method
    def start(self):
        try:
            # new API in Glyphs 2.3.1-910
            newMenuItem = NSMenuItem(self.name, self.showWindow)
            Glyphs.menu[EDIT_MENU].append(newMenuItem)
        except:
            mainMenu = Glyphs.mainMenu()
            s = objc.selector(self.showWindow,signature='v@:@')
            newMenuItem = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(self.name, s, "")
            newMenuItem.setTarget_(self)
            mainMenu.itemWithTag_(5).submenu().addItem_(newMenuItem)
    
    
    def loadPreferences(self):
        try:
            #Delete old settings (only manually called when needed)
            """del(Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.Preciseness"])
            del(Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.OverwriteDetected"])
            del(Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.Manual_i"])
            del(Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.Manual_I"])
            del(Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.DetectSerifs"])
            del(Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.TresholdStrokeLength"])
            del(Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.ScaleThickness"])
            del(Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.ScaleRest"])
            del(Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.ScaleSideBearings"])
            del(Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.ExtendStrokeWidth"])
            del(Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.MergeFiles"])
            del(Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.KeepWindowOpen"])
            del(Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.ExportLog"])"""
            #Set default settings
            NSUserDefaults.standardUserDefaults().registerDefaults_({
                "com.maartenrenckens.RhythmInfluencer.Preciseness": 1.0,
                "com.maartenrenckens.RhythmInfluencer.OverwriteDetected": True,
                "com.maartenrenckens.RhythmInfluencer.Manual_i": 40,
                "com.maartenrenckens.RhythmInfluencer.Manual_I": 50,
                "com.maartenrenckens.RhythmInfluencer.DetectSerifs": True,
                "com.maartenrenckens.RhythmInfluencer.TresholdStrokeLength": 150,
                "com.maartenrenckens.RhythmInfluencer.ScaleThickness": 100,
                "com.maartenrenckens.RhythmInfluencer.ScaleRest": 100,
                "com.maartenrenckens.RhythmInfluencer.ScaleSideBearings": 100,
                "com.maartenrenckens.RhythmInfluencer.ExtendStrokeWidth": 10,
                "com.maartenrenckens.RhythmInfluencer.MergeFiles": True,
                "com.maartenrenckens.RhythmInfluencer.KeepWindowOpen": True,
                "com.maartenrenckens.RhythmInfluencer.ExportLog": True
            })
            #Populate entry fields
            self.window.box_preciseness.set(Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.Preciseness"])
            """self.UIOverwriteDetected.setIntValue_(Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.OverwriteDetected"])
            self.UIManual_i.setStringValue_(Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.Manual_i"])
            self.UIManual_I.setStringValue_(Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.Manual_I"])
            self.UIDetectSerifs.setIntValue_(Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.DetectSerifs"])
            self.UITresholdStrokeLength.setStringValue_(Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.TresholdStrokeLength"])
            self.UIScaleThickness.setStringValue_(Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.ScaleThickness"])
            self.UIScaleRest.setStringValue_(Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.ScaleRest"])
            self.UIScaleSideBearings.setStringValue_(Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.ScaleSideBearings"])
            self.UIExtendStrokeWidth.setStringValue_(Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.ExtendStrokeWidth"])"""
            self.window.mergeFiles.set(Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.MergeFiles"])
            self.window.keepWindowOpen.set(Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.KeepWindowOpen"])
            self.window.ExportLog.set(Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.ExportLog"])
            
            if Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.ExportLog"]: print("Preferences loaded")
        except Exception, ex:
            print("Could not load prefs: %s" %ex)
    
    
    def savePreferences(self, sender):
        try:
            Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.Preciseness"] = self.window.box_preciseness.get()
            """Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.OverwriteDetected"] = self.UIOverwriteDetected.get()
            Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.Manual_i"] = self.UIManual_i.get()
            Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.Manual_I"] = self.UIManual_I.get()
            Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.DetectSerifs"] = self.UIDetectSerifs.get()
            Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.TresholdStrokeLength"] = self.UITresholdStrokeLength.get()
            Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.ScaleThickness"] = self.UIScaleThickness.get()
            Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.ScaleRest"] = self.UIScaleRest.get()
            Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.ScaleSideBearings"] = self.UIScaleSideBearings.get()
            Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.ExtendStrokeWidth"] = self.UIExtendStrokeWidth.get()"""
            Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.MergeFiles"] = self.window.mergeFiles.get()
            Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.KeepWindowOpen"] = self.window.keepWindowOpen.get()
            Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.ExportLog"] = self.window.ExportLog.get()
            
            if Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.ExportLog"]: print("Preferences saved: %s" %sender)
        except Exception, ex:
            print("Could not save prefs: %s" %ex)
    
    
    @objc.python_method
    def showWindow(self, sender):
        debug = Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.ExportLog"]
        if debug:
            Glyphs.showMacroWindow()
            Glyphs.clearLog()
            print("<<<The debug mode of the Rhythm Influencer is on.>>>")
        
        #general window info
        windowMargin = 15
        windowColumn1 = 285
        windowColumn2 = 100
        windowWidth = windowMargin*2 + windowColumn1 + windowColumn2
        windowExtraSpacer = 20
        windowRow1Plus = 40
        windowRow2Pos = windowMargin + windowRow1Plus
        windowRow2Plus = 65
        #Rows1
        windowRow3Pos = windowRow2Pos + windowRow2Plus + windowExtraSpacer
        windowRow3Plus = 20
        windowRow4Pos = windowRow3Pos + windowRow3Plus
        windowRow4Plus = 20
        #Rows2
        windowRow5Pos = windowRow4Pos + windowRow4Plus + windowExtraSpacer
        windowRow5Plus = 20
        
        windowHeight = 800
        
        #Closing notes (written in reverse order!)
        windowNotes1Min = 85
        windowNotes1Pos = windowHeight - windowNotes1Min
        windowNotes2Min = 20
        windowNotes2Pos = windowNotes1Pos - windowNotes2Min
        windowNotes3Min = 20
        windowNotes3Pos = windowNotes2Pos - windowNotes3Min
        windowNotes4Min = 50
        windowNotes4Pos = windowNotes3Pos - windowNotes4Min
        
        #Create the first window
        self.window = vanilla.FloatingWindow(
            (windowWidth, windowHeight),
            "Rhythm Influencer", #Title Bar Title
            autosaveName = "com.maartenrenckens.RhythmInfluencer.mainwindow"
        )
        
        ########################
        # General introduction #
        ########################
        
        self.window.text_1 = vanilla.TextBox( (windowMargin, windowMargin, -windowMargin, windowRow1Plus), "The Rhythm Influencer creates variations on the rhythm in (most) letters fast. BETA version!", sizeStyle='regular')
        self.window.text_2 = vanilla.TextBox( (windowMargin, windowRow2Pos, -windowMargin, windowRow2Plus), "The app understands the rhythm in letters via an analysis of the black mass. Based on the highest concentration of this black mass, the rhythm in the letters is derrived. Knowing the rhythm allows for fast transformations in the letter shapes.", sizeStyle='small')
        
        ###############
        # Preciseness #
        ###############
        
        self.window.text_Row2 = vanilla.TextBox( (windowMargin, windowRow3Pos, -windowMargin, windowRow3Plus), "Preciseness (in Em units):", sizeStyle='small')
        self.window.box_preciseness = vanilla.EditText( (windowColumn1, windowRow3Pos, -windowMargin, windowRow3Plus-1), sizeStyle='small')
        self.window.text_Row3 = vanilla.TextBox( (windowMargin, windowRow4Pos, -windowMargin, windowRow4Plus), "Angle: (not yet implemented in this version of the plugin)", sizeStyle='small')
        """X"""
        
        #######################
        # Draw the black mass #
        #######################
        
        self.window.DrawBlackMass = vanilla.Button( (windowMargin, windowRow5Pos, -windowMargin, windowRow5Plus), "Draw the black mass distribution for the selected glyphs", callback=self.WorkOnBlackMass, sizeStyle='small')
        
        ###################
        # Draw the rhythm #
        ###################
        
        
        
        #################
        # Closing notes #
        #################
        
        self.window.mergeFiles = vanilla.CheckBox( (windowMargin, windowNotes4Pos, -windowMargin, windowNotes4Min), "Merge different drawings into one file\nFor example: capitals require other scales, round letters could use an angle,… Select and process those separatedly.", callback=self.savePreferences, sizeStyle='small')
        self.window.keepWindowOpen = vanilla.CheckBox( (windowMargin, windowNotes3Pos, -windowMargin, windowNotes3Min), "Keep this window open on finish", callback=self.savePreferences, sizeStyle='small' )
        self.window.ExportLog = vanilla.CheckBox( (windowMargin, windowNotes2Pos, -windowMargin, windowNotes2Min), "Export a log to the console", callback=self.savePreferences, sizeStyle='small' )
        self.window.text_notes1 = vanilla.TextBox( (windowMargin, windowNotes1Pos, -windowMargin, windowNotes1Min), "Rhythm Influencer: copyright Maarten Renckens (Artengar) 2020. Free to use, but all rights reserved. Use it with a correct reference. Thanks for your respect. For more info, bug reports, suggestions or gifts to enable further development: maarten.renckens@artengar.com.", sizeStyle='small')
        
        #Render the window
        self.loadPreferences()
        self.window.open()
        self.window.makeKey()
    
    
    def WorkOnBlackMass(self, sender):
        if Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.ExportLog"]: print("\n<<<Starting Drawing a mass>>>")
        main_steps(makeDistribution=True, makeRhythm=False, makeScale=False)
        if Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.KeepWindowOpen"] == 0:
            self.close()
    
    def WorkOnRhythm(self, sender):
        if Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.ExportLog"]: print("\n<<<Starting Drawing a rhythm>>>")
        if Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.OverwriteDetected"] == False:
            detectStrokeThicknesses(debug, self, Active_Font)
        main_steps(makeDistribution=False, makeRhythm=True, makeScale=False)
        if Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.KeepWindowOpen"] == 0:
            self.close()
    
    def WorkOnScaling(self, sender):
        if Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.ExportLog"]: print("\n<<<Starting Drawing a scaled font>>>")
        if Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.OverwriteDetected"] == False:
            detectStrokeThicknesses(debug, self, Active_Font)
        main_steps(makeDistribution=False, makeRhythm=False, makeScale=True)
        if Glyphs.defaults["com.maartenrenckens.RhythmInfluencer.KeepWindowOpen"] == 0:
            self.close()
    
    
    @objc.python_method
    def __file__(self):
        """Please leave this method unchanged"""
        return __file__
    