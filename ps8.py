# 6.00 Problem Set 8
#
# Name: Niki Castle
# Collaborators: debugging help from Rui Hu
# Time: ~15hrs



import numpy
import random
import pylab
from ps7 import *

#
# PROBLEM 1
#
class ResistantVirus(SimpleVirus):

    """
    Representation of a virus which can have drug resistance.
    """      

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):

        """

        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'grimpex',False}, means that this virus
        particle is resistant to neither guttagonol nor grimpex.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.        

        """


        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb



    def isResistantTo(self, drug):

        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in Patient to determine how many virus
        particles have resistance to a drug.    

        drug: The drug (a string)
        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        return self.resistances[drug]


    def reproduce(self, popDensity, activeDrugs):

        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient class.

        If the virus particle is not resistant to any drug in activeDrugs,
        then it does not reproduce. Otherwise, the virus particle reproduces
        with probability:       
        
        self.maxBirthProb * (1 - popDensity).                       
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). 

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.        

        For example, if a virus particle is resistant to guttagonol but not
        grimpex, and `self.mutProb` is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90% 
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        grimpex and a 90% chance that the offspring will not be resistant to
        grimpex.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population        

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings). 
        
        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.         
        """
        childsResistances = {}
        for drug in activeDrugs:
            if not self.isResistantTo(drug):
                raise NoChildException()
        if random.random() <= self.maxBirthProb*(1-popDensity):
            for drug in self.resistances:
                if random.random() <= self.mutProb:
                    childsResistances[drug] = not self.isResistantTo(drug)
                else:
                    childsResistances[drug] = self.isResistantTo(drug)
            return ResistantVirus(self.maxBirthProb, self.clearProb, childsResistances, self.mutProb)
        else:
            raise NoChildException()

class Patient(SimplePatient):

    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).               

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)
        
        maxPop: the  maximum virus population for this patient (an integer)
        """
        #SimplePatient.__init__(self, viruses, maxPop)
        self.viruses = viruses
        self.maxPop = maxPop
        self.activeDrugs = []
    

    def addPrescription(self, newDrug):

        """
        Administer a drug to this patient. After a prescription is added, the 
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: list of drugs being administered to a patient is updated
        """
        if newDrug not in self.activeDrugs:
            self.activeDrugs.append(newDrug)


    def getPrescriptions(self):

        """
        Returns the drugs that are being administered to this patient.
        returns: The list of drug names (strings) being administered to this
        patient.
        """

        return self.activeDrugs
        

    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in 
        drugResist.        

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'grimpex'])

        returns: the population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        resistantViruses = []
        for virus in self.viruses:
            for drug in drugResist:
                if not virus.isResistantTo(drug):
                    break
                elif drug == drugResist[len(drugResist)-1]:
                    resistantViruses.append(virus)
        return len(resistantViruses)
                   


    def update(self):

        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:
        
        - Determine whether each virus particle survives and update the list of 
          virus particles accordingly          
        - The current population density is calculated. This population density
          value is used until the next call to update().
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient. 
          The listof drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces. 

        returns: the total virus population at the end of the update (an
        integer)
        """
        newViruses = []
        for virus in self.viruses:
            if not virus.doesClear():
                newViruses.append(virus)
                
        popDensity = float(len(newViruses))/self.maxPop
        self.viruses = [x for x in newViruses]
        #remainingViruses = len(self.newViruses)
        for virus in self.viruses:
            try:
               # newViruses.append(virus.reproduce(popDensity, self.activeDrugs))
                toadd = virus.reproduce(popDensity, self.activeDrugs)
                newViruses.append(toadd)
            except NoChildException:
                pass
        self.viruses = [x for x in newViruses]
        return len(self.viruses)



#
# PROBLEM 2
#

def simulationWithDrug():

    """

    Runs simulations and plots graphs for problem 4.
    Instantiates a patient, runs a simulation for 150 timesteps, adds
    guttagonol, and runs the simulation for an additional 150 timesteps.
    total virus population vs. time and guttagonol-resistant virus population
    vs. time are plotted
    """
    #initiate lists for plotting purposes
    allViruses = []
    resistantViruses = []
    averageViruses = []
    averageResistantViruses = []
    #initiate parameters
    viruses = []
    timesteps = []
    resistances = {'guttagonol' : False}
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    mutProb = 0.005
    timeBeforeDrug = 150
    timeAfterDrug = 150
    #number of trials to take the average of
    reps = 1
    #create our patient
    patient = Patient(viruses, maxPop)
    #set up our lists
    #timesteps will have all the times in our range
    #allViruses and resistantViruses start out with 0 for each time
    for time in range(timeBeforeDrug + timeAfterDrug):
        timesteps.append(time)
        allViruses.append(0)
        resistantViruses.append(0)
        averageViruses.append(0)
        averageResistantViruses.append(0)
    #run simulation 'reps' times
    for rep in range(reps):
        #initiate 100 viruses
        for i in range(100):
            viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
        #add to totals for each timestep before guttagonol is prescribed
        for j in range(timeBeforeDrug):
            allViruses[j] += patient.update()
            resistantViruses[j] += patient.getResistPop(['guttagonol'])
        #prescribe guttagonol
        patient.addPrescription('guttagonol')
        #add to totals for each timestep after guttagonol is prescribed
        for k in range(timeBeforeDrug, timeBeforeDrug+timeAfterDrug):
            allViruses[k] += patient.update()
            resistantViruses[k] += patient.getResistPop(['guttagonol'])
    #average values for each timestep over number of trials
    print allViruses
    print resistantViruses
    for time in range(timeBeforeDrug + timeAfterDrug):
        averageViruses[time] = float(allViruses[time])/reps
        averageResistantViruses[time] = float(resistantViruses[time])/reps
    #plot both graphs
    pylab.plot(timesteps, averageViruses)
    pylab.plot(timesteps, averageResistantViruses)
    pylab.title('Virus Population Change over Time')
    pylab.xlabel('# of Timesteps Elapsed')
    pylab.legend(('Viruses', 'Resistant Viruses'))
    pylab.show()


#
# PROBLEM 3
#        

def simulationDelayedTreatment():

    """
    Runs simulations and make histograms for problem 5.
    Runs multiple simulations to show the relationship between delayed treatment
    and patient outcome.
    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).    
    """

    #initiate parameters
    finalViruses = []
    viruses = []
    timesteps = []
    resistances = {'guttagonol' : False}
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    mutProb = 0.005
    timeBeforeDrug = 300
    timeAfterDrug = 150
    #number of trials to take the average of
    reps = 100
    #create our patient
    patient = Patient(viruses, maxPop)
    #timesteps will have all the times in our range
    for time in range(timeBeforeDrug + timeAfterDrug):
        timesteps.append(time)
    #run simulation 'reps' times
    for rep in range(reps):
        print "Patient number ",rep
        #initiate 100 viruses
        for i in range(100):
            viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
        for j in range(timeBeforeDrug):
            patient.update()
        #prescribe guttagonol
        patient.addPrescription('guttagonol')
        for k in range(timeBeforeDrug, timeBeforeDrug+timeAfterDrug):
            patient.update()
        finalViruses.append(patient.update())
        print "Viruses are",finalViruses
    pylab.hist(finalViruses, 10)
    pylab.title('Viruses after 150 Timesteps')
    pylab.xlabel('# of Viruses')
    pylab.ylabel('# of Patients')
    pylab.show()

#
# PROBLEM 4
#

def simulationTwoDrugsDelayedTreatment():

    """
    Runs simulations and make histograms for problem 6.
    Runs multiple simulations to show the relationship between administration
    of multiple drugs and patient outcome.
   
    Histograms of final total virus populations are displayed for lag times of
    150, 75, 0 timesteps between adding drugs (followed by an additional 150
    timesteps of simulation).
    """

    viruses = []
    timesteps = []
    finalViruses = []
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol':False, 'grimpex':False}
    mutProb = 0.005
    reps = 100
    timeBeforeGuttagonol = 150
    timeBeforeGrimpex = 150
    timeAfterDrugs = 150
    patient = Patient(viruses, maxPop)
    for time in range(timeBeforeGrimpex + timeAfterDrugs):
        timesteps.append(time)
    for rep in range(reps):
        for i in range(100):
            viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))    
        for j in range(timeBeforeGuttagonol):
            patient.update()
        patient.addPrescription('guttagonol')
        for j in range(timeBeforeGuttagonol, timeBeforeGrimpex):
            patient.update()
        patient.addPrescription('grimpex')
        for j in range(timeBeforeGrimpex, timeAfterDrugs):
            patient.update()
        finalViruses.append(patient.update())
    pylab.hist(finalViruses, 10)
    pylab.title('Viruses after 300 Timesteps')
    pylab.xlabel('# of Viruses')
    pylab.ylabel('# of Patients')
    pylab.show()


#
# PROBLEM 5
#    

def simulationTwoDrugsVirusPopulations():

    """

    Run simulations and plot graphs examining the relationship between
    administration of multiple drugs and patient outcome.
    Plots of total and drug-resistant viruses vs. time are made for a
    simulation with a 300 time step delay between administering the 2 drugs and
    a simulations for which drugs are administered simultaneously.        

    """
    #initialize lists for plotting purposes
    allViruses = []
    dualResistantViruses = []
    grimpexResistantViruses = []
    guttagonolResistantViruses = []
    averageViruses = []
    avgGrimResViruses = []
    avgGuttagResViruses = []
    avgDualResViruses = []
    #initialize parameters
    viruses = []
    timesteps = []
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol':False, 'grimpex':False}
    mutProb = 0.005
    reps = 1
    timeBeforeGuttagonol = 150
    timeBeforeGrimpex = 150
    timeAfterDrugs = 150
    patient = Patient(viruses, maxPop)
    #create elements of plotting lists for each timestep
    for time in range(timeBeforeGrimpex + timeAfterDrugs):
        timesteps.append(time)
        allViruses.append(0)
        dualResistantViruses.append(0)
        grimpexResistantViruses.append(0)
        guttagonolResistantViruses.append(0)
        averageViruses.append(0)
        avgGrimResViruses.append(0)
        avgGuttagResViruses.append(0)
        avgDualResViruses.append(0)
    for rep in range(reps):
        for i in range(100):
            viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
        #update for every timestep before guttagonol is prescribed
        for j in range(timeBeforeGuttagonol):
            allViruses[j] += patient.update()
            guttagonolResistantViruses[j] += patient.getResistPop(['guttagonol'])
            grimpexResistantViruses[j] += patient.getResistPop(['grimpex'])
            dualResistantViruses[j] += patient.getResistPop(['guttagonol', 'grimpex'])
        patient.addPrescription('guttagonol')
        #update for every timestep before grimpex is prescribed
        for j in range(timeBeforeGuttagonol, timeBeforeGrimpex):
            allViruses[j] += patient.update()
            guttagonolResistantViruses[j] += patient.getResistPop(['guttagonol'])
            grimpexResistantViruses[j] += patient.getResistPop(['grimpex'])
            dualResistantViruses[j] += patient.getResistPop(['guttagonol', 'grimpex'])
        patient.addPrescription('grimpex')
        #update for every timestep after both drugs are prescribed
        for j in range(timeBeforeGrimpex, timeAfterDrugs):
            allViruses[j] += patient.update()
            guttagonolResistantViruses[j] += patient.getResistPop(['guttagonol'])
            grimpexResistantViruses[j] += patient.getResistPop(['grimpex'])
            dualResistantViruses[j] += patient.getResistPop(['guttagonol', 'grimpex'])
    #take average of all totals
    for time in range(timeBeforeGrimpex + timeAfterDrugs):
        averageViruses[time] = float(allViruses[time])/reps
        avgGrimResViruses[time] = float(grimpexResistantViruses[time])/reps
        avgGuttagResViruses[time] = float(guttagonolResistantViruses[time])/reps
        avgDualResViruses[time] = float(dualResistantViruses[time])/reps
    pylab.plot(timesteps, averageViruses)
    pylab.plot(timesteps, avgGrimResViruses)
    pylab.plot(timesteps, avgGuttagResViruses)
    pylab.plot(timesteps, avgDualResViruses)
    pylab.title('Virus Population Change over Time')
    pylab.xlabel('# of Timesteps Elapsed')
    pylab.legend(('Viruses', 'Grimpex-Resistant Viruses', 'Guttagonol-Resistant Viruses', 'Dual-Resistant Viruses'))
    pylab.show()
#simulationDelayedTreatment()
#simulationTwoDrugsVirusPopulations()
