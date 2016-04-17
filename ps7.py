# Problem Set 7: Simulating the Spread of Disease and Virus Population Dynamics 
# Name: Niki Castle
# Collaborators: none
# Time: ~7hrs

import numpy
import random
import pylab

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 1
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):

        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """

        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def doesClear(self):

        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.clearProb and otherwise returns
        False.
        """

        if random.random() <= self.clearProb:
            return True
        else:
            return False

    
    def reproduce(self, popDensity):

        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the SimplePatient and
        Patient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """

        if random.random() <= self.maxBirthProb*(1-popDensity):
            return SimpleVirus(self.maxBirthProb, self.clearProb)
        else:
            raise NoChildException()



class SimplePatient(object):

    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):

        """

        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the  maximum virus population for this patient (an integer)
        """

        self.viruses = viruses
        self.maxPop = maxPop
        self.population = len(self.viruses)


    def getTotalPop(self):

        """
        Gets the current total virus population. 
        returns: The total virus population (an integer)
        """
        return self.population
                


    def update(self):

        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """
        #make a new list
        self.newViruses = []
        #add all viruses from old list that didn't die
        for virus in self.viruses:
            if not virus.doesClear():
                self.newViruses.append(virus)
        #update population density
        popDensity = float(len(self.newViruses))/self.maxPop
        #update virus list
        self.viruses = self.newViruses
        #each virus that hasn't died tries to reproduce
        for virus in self.viruses:
            try:
                self.newViruses.append(virus.reproduce(popDensity))
            except NoChildException:
                pass
        #update virus list again
        self.viruses = self.newViruses
        return len(self.viruses)
            

#
# PROBLEM 2
#
def simulationWithoutDrug():

    """
    Run the simulation and plot the graph for problem 2 (no drugs are used,
    viruses do not have any drug resistance).    
    Instantiates a patient, runs a simulation for 300 timesteps, and plots the
    total virus population as a function of time.    
    """
    #create lists for viruses, timesteps, and numbers of viruses
    viruses = []
    timesteps = []
    numbers = []
    #set max population, max birthrate, and probability of death
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    #initiate patient
    patient = SimplePatient(viruses, maxPop)
    #initiate a list of 100 viruses
    for i in range(100):
        viruses.append(SimpleVirus(maxBirthProb, clearProb))
    #create list of virus counts corresponding to each of 300 timesteps
    for j in range(300):
        timesteps.append(j)
        numbers.append(patient.update())
    ###USED FOR GRAPH:
    ###return numbers
    #graph virus population against time
    pylab.plot(timesteps, numbers)
    pylab.title('Virus Population Change Over Time')
    pylab.xlabel('# of Timesteps Elapsed')
    pylab.ylabel('Virus Population')
    pylab.show()

#simulationWithoutDrug()


##USED FOR GRAPH
##
##
##averages = []
##totals = []
##timesteps = []
##reps = 100
##for i in range(300):
##    timesteps.append(i)
##    totals.append(0)
##for j in range(reps):
##    trial = simulationWithoutDrug()
##    for i in range(300):
##        totals[i] += trial[i]
##for k in totals:
##    averages.append(k/reps)
##pylab.plot(timesteps, averages)
##pylab.title('Virus Population Change Over Time')
##pylab.xlabel('# of Timesteps Elapsed')
##pylab.ylabel('Average Virus Population')
##pylab.show()
