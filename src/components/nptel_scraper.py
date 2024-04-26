import json
import random
import regex

text = '''
1 Which of these is not a characteristic of fitness?
a. Fitness is environment-specific.
b. Fitness is species-specific.
c. Higher reproductive rate means higher fitness.
d. Fitness should be measured across several generations.
2 Ecology is the scientific study of interactions among organisms and their ___. (Fill in the blanks)
a. habitat
b. niche
c. environment
d. population
3 "Enquiry into plants" is a book written by
a. Theophrastus
b. Linnaeus
c. Malthus
d. Humboldt
4 Which of these is not a kind of selection
a. directional
b. stochastic
c. disruptive
d. stabilising
5 Ecology is the scientific study of ___ that determine the distribution and abundance of organisms. (Fill in the blanks)
a. statics
b. interactions
c. dynamics
d. habitat
6 Which of these is not a step in natural selection?
a. variation
b. underpopulation
c. struggle for existence
d. survival of the fittest
7 Which of these is not a characteristic of fitness?
a. Fitness is environment-specific.
b. Fitness is species-specific.
c. Fitness works on traits such as size and speed.
d. Fitness should be measured across several generations.
8 In the Greek word root of Ecology, Oikos refers to
a. household
b. preservation
c. environment
d. study
9 In the Greek word root of Ecology, logos refers to
a. household
b. preservation
c. environment
d. study
10 Who amongst these is considered the father of Biogeography?
a. Theophrastus
b. Linnaeus
c. Malthus
d. Humboldt

1 For more biodiversity, the level of disturbance should be
a. less
b. intermediate
c. more
d. none of these
2 Hierarchy emerges almost inevitably through a wide variety of evolutionary processes, for the simple reason that hierarchical structures are ___ (Fill in the blank)
a. perfect
b. imperfect
c. stable
d. unstable
3 "groups of actually or potentially interbreeding natural populations, which are reproductively isolated from other such groups" is a definition of
a. cells
b. species
c. ecosystems
d. biomes
4 The emergent principle can be stated as
a. Whole = sum of parts
b. Whole < sum of parts
c. Whole > sum of parts
d. None of these
5 There is more biodiversity in areas with
a. less competition, less predation
b. less competition, more predation
c. more competition, more predation
d. more competition, less predation
6 The mitochondrion is a / an
a. Sub-cellular organelle
b. Cell
c. Tissue
d. Organ
7 "the diversity that exists among different geographies" is
a. alpha (α) biodiversity
b. beta (β) biodiversity
c. gamma (γ) biodiversity
d. delta (δ) biodiversity
8 "the diversity that exists within an ecosystem" is
a. alpha (α) biodiversity
b. beta (β) biodiversity
c. gamma (γ) biodiversity
d. delta (δ) biodiversity
9 The hierarchical system was given by
a. Simon
b. Watson
c. Hutchinson
d. Humboldt
10 The laboratory approach to Ecology uses
a. equations
b. models
c. observations
d. experiments

1 I observe a bird take a tick out of another bird's head and eat it. In the social context, this behaviour would be called
a. tick hunting
b. auto grooming
c. allo grooming
d. foraging
2 The scientific study of animal behaviour is called
a. behaviourism
b. ecology
c. ethology
d. prey-predator dynamics
3 Trampling of grass due to the movement of animals is an example of
a. mutualism
b. amensalism
c. commensalism
d. protocooperation
4 Birds on giraffe are an example of
a. colony
b. commensalism
c. protocooperation
d. allelopathy
5 I observe a monkey take a tick out of another monkey's head and eat it. In the social context, this behaviour would be called
a. tick hunting
b. auto grooming
c. allo grooming
d. foraging
6 Hamilton's rule can be stated as
a. rB < C
b. rB > C
c. rB = C
d. rB + C = 0
7 Egrets with buffaloes are an example of
a. colony
b. commensalism
c. protocooperation
d. allelopathy
8 The interaction between exotic shrubs and trees through the action of seed predators is an example of
a. infraspecific competition
b. apparent competition
c. disguised competition
d. harmonious competition
9 Harmonious interactions occur where
a. at least one participant is benefited
b. at least one participant is unharmed
c. both participants are benefitted
d. both participants are unharmed
10 An inventory of behaviours exhibited by an animal during a behaviour exercise is called
a. ecogram
b. ethogram
c. behaviourogram
d. animalogram

1 Tree → Frugivorous birds → Hawk represents
a. upright pyramid of numbers
b. inverted pyramid of numbers
c. spindle pyramid of numbers
d. dumb-bell pyramid of numbers
2 If we all became vegetarians, we'll be able to support our large populations. This can be explained through
a. 10% rule
b. 1% rule
c. trophic cascade
d. biodiversity
3 Consider the food chain: Grass → Grasshopper → Frog → Snake →Hawk. As we move up the food chain, 
a. available energy decreases
b. available energy increases
c. available energy remains same
d. available energy is zero everywhere
4 Glacial lakes are typical examples of
a. eutrophic lakes
b. hypereutrophic lakes
c. oligotrophic lakes
d. mesotrophic lakes
5 Trees → Birds → Parasites → Hyperparasites represents
a. upright pyramid of numbers
b. inverted pyramid of numbers
c. spindle pyramid of numbers
d. dumb-bell pyramid of numbers
6 Consider the food chain: Grass → Grasshopper → Frog → Snake →Hawk. In this food chain, 
a. frog is producer
b. frog is consumer and carnivore
c. frog is consumer and herbivore
d. frog is decomposer
7 At the compensation point, 
a. photosynthesis = respiration
b. photosynthesis < respiration
c. photosynthesis > respiration
d. photosynthesis = 0
8 Consider the food chain: Grass → Grasshopper → Frog → Snake →Hawk. In this food chain, 
a. more number of hawks than grasshoppers can be supported
b. more number of grasshoppers than hawks can be supported
c. equal number of hawks and grasshoppers can be supported
d. none of these
9 Consider the food chain: Grass → Grasshopper → Frog → Snake →Hawk. In this food chain, 
a. hawk is producer
b. hawk is consumer and carnivore
c. hawk is consumer and herbivore
d. hawk is decomposer
10 Net primary productivity is given by
a. APAR × LUE
b. APAR + LUE
c. APAR - LUE
d. APAR / LUE

1 Which of these is not a measure of absolute population density?
a. total count
b. pelt count
c. capture-recapture method
d. removal method
2 The juvenile mortality rate is the annual number of deaths of juveniles per
a. 100 births
b. 1000 births
c. 100 live births
d. 1000 live births
3 ___ is how close the measured values are to the correct value.
a. Accuracy
b. Precision
c. Bias
d. Variance
4 ___ employs a simple rule of selecting every kth unit starting with a number chosen at random from 1 to k as the random start.
a. Simple random sampling
b. Systematic sampling
c. Stratified sampling
d. Multistage sampling
5 Cover board surveys are typically used for sampling
a. herpetofauna
b. fishes
c. large mammals
d. carnivores
6 The minimum replacement level fertility for a population to grow should be greater than
a. 1
b. 2
c. 3
d. 4
7 The logistic growth equation, when plotted, appears
a. I shaped
b. J shaped
c. S shaped
d. O shaped
8 Pan traps are used for sampling
a. bees
b. butterflies
c. non-pollinator insects
d. pollinator insects
9 A sampling procedure such that each possible combination of sampling units out of the population has the same chance of being selected is referred to as
a. Simple random sampling
b. Systematic sampling
c. Stratified sampling
d. Multistage sampling
10 Which of these is true?
a. Physiological longevity > Ecological longevity
b. Physiological longevity = Ecological longevity
c. Physiological longevity < Ecological longevity
d. a or b

1 Importance value varies from
a. 0 to 10
b. 0 to 50
c. 0 to 100
d. 0 to 300
2 A species found most frequently in a particular community, but also present occasionally in others is called
a. accidental species
b. indifferent species
c. selective species
d. exclusive species
3 Which of these depicts correctly the lithosere primary succession?
a. Rock → Crustose lichen → Foliose lichen → Moss →Herbaceous stage → Shrub → Woodland → Climax
b. Rock → Foliose lichen → Crustose lichen → Moss →Herbaceous stage → Shrub → Woodland → Climax
c. Moss → Crustose lichen → Foliose lichen → Rock →Herbaceous stage → Shrub → Woodland → Climax
d. Rock → Crustose lichen → Foliose lichen → Shrub →Herbaceous stage → Moss → Woodland → Climax
4 Importance value can be written as
a. Relative density + Relative frequency X Relative dominance
b. Relative density X Relative frequency + Relative dominance
c. Relative density + Relative frequency + Relative dominance
d. Relative density X Relative frequency X Relative dominance
5 Lithosere is an example of
a. hydrosere
b. xerosere
c. psammosere
d. halosere
6 The climax near Tindni village is being controlled by disturbance by cattle. This is an example of
a. climatic climax
b. edaphic climax
c. disclimax
d. catastrophic climax
7 A climax caused by wildfires is an example of
a. climatic climax
b. edaphic climax
c. disclimax
d. catastrophic climax
8 Which of these is correct?
a. Fundamental niche > Realised niche
b. Fundamental niche = Realised niche
c. Fundamental niche < Realised niche
d. a or b
9 When compared to generalist species, specialist species have
a. narrower niches
b. broader niches
c. same-size niches
d. none of these
10 Which of these is not a characteristic of pioneer species
a. ability to grow on bare rocks
b. ability to tolerate extreme temperatures
c. large size
d. short life span

1 Scarcity of food is a
a. chemical factor
b. demographic factor
c. push factor
d. pull factor
2 Good climate is a
a. chemical factor
b. demographic factor
c. push factor
d. pull factor
3 The movement of individuals away from their place of birth or hatching or seed production into a new habitat or area to survive and reproduce is called
a. translocation
b. migration
c. dispersal
d. drifting
4 "The geographical distribution of a species will be controlled by that environmental factor for which the organism has the narrowest range of tolerance." This is the statement for
a. Liebig’s law of the minimum
b. Liebig’s law of the maximum
c. Shelford’s law of tolerance
d. Shelford’s law of intolerance
5 "Quick movement over large distances, often across unsuitable terrain" is a description of
a. diffusion
b. secular dispersal
c. jump dispersal
d. drifting
6 The regular, seasonal movement of animals, often along fixed routes is called
a. translocation
b. migration
c. dispersal
d. drifting
7 The movement of lions across the Gir landscape is an example of
a. diffusion
b. secular dispersal
c. jump dispersal
d. drifting
8 Which of these is not a physical factor of habitat?
a. soil
b. moisture
c. predators
d. temperature
9 Transplantation experiments are used to find
a. potential range
b. effective range
c. actual range
d. economic range
10 I tried growing vegetables under my teak plantation, but the vegetable plants died out. I should be concerned about
a. autophagy
b. allelophagy
c. autopathy
d. allelopathy

1 Captive breeding is an example of
a. in-situ conservation
b. ex-situ conservation
c. in-situ preservation
d. ex-situ preservation
2 The “subset of physical and biotic environmental factors that permit an animal (or plant) to survive and reproduce” is the definition of
a. habitat
b. ecosystem
c. biome
d. biosphere
3 We prefer those areas for the creation of a conservation reserve where the level of threat is
a. very high
b. medium
c. very low
d. non-existent
4 Which of these is a deterministic factor?
a. environmental variation
b. forest fire
c. death rate
d. diseases
5 The acronym HIPPO does not include
a. habitat loss
b. habitat enhancement
c. invasive species
d. human over-population
6 Which of these correctly represents the process of habitat fragmentation and loss?
a. Original forest → Dissection → Perforation → Fragmentation → Attrition
b. Original forest → Dissection → Attrition → Fragmentation →Perforation
c. Original forest → Dissection → Perforation → Attrition →Fragmentation
d. Original forest → Dissection → Fragmentation → Perforation →Attrition
7 The acronym HIPPO does not include
a. habitat loss
b. invasive species
c. pollination
d. pollution
8 Which of these is a stochastic factor?
a. birth rate
b. death rate
c. population structure
d. environmental fluctuation
9 According to Leopold, which of these is not a tool of habitat management?
a. fire
b. gun
c. cattle
d. sickle
10 Zoo is an example of
a. in-situ conservation
b. ex-situ conservation
c. in-situ preservation
d. ex-situ preservation

1 Which of these is a preventive check according to Malthus?
a. foresight
b. vice
c. misery
d. flood
2 Which of these is not a pillar of sustainability?
a. environmental sustainability
b. economic sustainability
c. trans-boundary sustainability
d. social sustainability
3 ___ is used to identify which potential impacts are relevant to assess. (Fill in the blank)
a. screening
b. scoping
c. reporting
d. review
4 Which of these is a positive check according to Malthus?
a. late marriage
b. war
c. celibacy
d. moral restraint
5 Which of these is a pillar of sustainability
a. social sustainability
b. industrial sustainability
c. agricultural sustainability
d. trans-boundary sustainability
6 The demographic transition sees a society move from
a. high birth rate, low death rate to low birth rate, low death rate
b. low birth rate, high death rate to low birth rate, low death rate
c. high birth rate, high death rate to low birth rate, low death rate
d. high birth rate, high death rate to low birth rate, high death rate
7 The book "An Essay on the Principle of Population" was written by
a. Darwin
b. Malthus
c. Spencer
d. Owens
8 The quantum of human impacts is given by
a. I = P × A × T
b. I = P + A + T
c. I = P + A - T
d. I = P - (A + T)
9 ___ determines which projects or developments require a full or partial impact assessment study. (Fill in the blank)
a. screening
b. scoping
c. reporting
d. review
10 According to Malthusian model, 
a. Population grows in geometric progression, food supply increases in arithmetic progression
b. Population grows in geometric progression, food supply increases in geometric progression
c. Population grows in arithmetic progression, food supply increases in arithmetic progression
d. Population grows in arithmetic progression, food supply increases in geometric progression

1 Mesodebris in the context of plastic debris has fragments of size
a. > 20 mm
b. 5 - 20 mm
c. < 5 mm
d. < 1 mm
2 The government came up with a regulation that incandescent bulbs be replaced by LED bulbs, so that electricity consumption and release of carbon dioxide from power plants is reduced. In the context of climate change, such an action would be called
a. adaptation
b. mitigation
c. deceleration
d. maladaptation
3 Which of these is not a climatic forcing for Earth?
a. changes in plate tectonics
b. changes in Earth's orbit
c. changes in Moon's orbit
d. changes in Sun's strength
4 Which of these is not a principle of ecological restoration?
a. ecological integrity
b. long-term sustainability
c. benefits and engages scientists
d. informed by past and future
5 “The ability of a system to adjust to climate change (including climate variability and extremes) to moderate potential damages, to take advantage of opportunities, or to cope with the consequences” is a definition for
a. adaptive response
b. adaptive capacity
c. mitigative response
d. mitigative capacity
6 Which of these is not a principle of ecological restoration?
a. ecological integrity
b. short-term sustainability
c. benefits and engages society
d. informed by past and future
7 Macrodebris in the context of plastic debris has fragments of size
a. > 20 mm
b. 5 - 20 mm
c. < 5 mm
d. < 1 mm
8 Because of climate change, Mudumalai Tiger Reserve is suffering from frequent droughts. The management has built several artificial water holes for animals, and fills them up regularly with tankers. In the context of climate change, such an action would be called
a. adaptation
b. mitigation
c. deceleration
d. maladaptation
9 “Any changes in natural or human systems that inadvertently increase vulnerability to climatic stimuli; an adaptation that does not succeed in reducing vulnerability but increases it instead” is a definition for
a. adaptation
b. mitigation
c. maladaptation
d. malmitigation
10 Which of these is not a climatic forcing for Earth?
a. changes in plate tectonics
b. changes in Earth's orbit
c. changes in Sun's orbit
d. changes in Sun's strength

1 A pest population is called uncontrolled when
a. it is increasing
b. it is not decreasing
c. it is causing some economic damage
d. it is causing excessive economic damage
2 The impact of El Nino on fishery collapse in Peru is explained by
a. match hypothesis
b. mismatch hypothesis
c. match-mismatch hypothesis
d. none of these
3 Which of these is correct?
a. R + G = M + F
b. R + M = G + F
c. R + F = M + G
d. R + G + M + F = 0
4 Ludwig's ratchet predicts
a. decreasing harvesting rate
b. constant harvesting rate
c. increasing harvesting rate
d. fluctuating harvesting rate
5 A root zone treatment plant is an example of
a. phytoremediation
b. biological control
c. biomagnification
d. bioaccumulation
6 A pest population is called controlled when
a. it is not increasing
b. it is decreasing
c. it is not causing any economic damage
d. it is not causing excessive economic damage
7 A deciduous forest in Madhya Pradesh was converted to a mine. After the mining operations were over, the pits were filled up with water and a lake was created. It is now visited by several migratory birds. This is an example of
a. recovery
b. restoration
c. enhancement
d. replacement
8 A deciduous forest in Madhya Pradesh was converted to a mine. After the mining operations were over, the pits were filled up with soil and species of deciduous forest planted again. This is an example of
a. recovery
b. restoration
c. enhancement
d. replacement
9 Which of these is not an impact of toxic chemicals?
a. lethal effects
b. sub-lethal effects
c. reduction of existing stressors
d. reduced fecundity
10 Which of these is correct?
a. The maximum sustainable yield is near the beginning of the sigmoidal curve.
b. The maximum sustainable yield is near the mid-point of the sigmoidal curve.
c. The maximum sustainable yield is near the end of the sigmoidal curve.
d. None of these.

1 Hierarchy emerges almost inevitably through a wide variety of evolutionary processes, for the simple reason that hierarchical structures are ___ (Fill in the blank)
a. perfect
b. imperfect
c. stable
d. unstable
2 Which of these is a stochastic factor?
a. birth rate
b. death rate
c. population structure
d. environmental fluctuation
3 The climax near Tindni village is being controlled by disturbance by cattle. This is an example of
a. climatic climax
b. edaphic climax
c. disclimax
d. catastrophic climax
4 ___ determines which projects or developments require a full or partial impact assessment study. (Fill in the blank)
a. screening
b. scoping
c. reporting
d. review
5 The movement of lions across the Gir landscape is an example of
a. diffusion
b. secular dispersal
c. jump dispersal
d. drifting
6 Trampling of grass due to the movement of animals is an example of
a. mutualism
b. amensalism
c. commensalism
d. protocooperation
7 Cover board surveys are typically used for sampling
a. herpetofauna
b. fishes
c. large mammals
d. carnivores
8 Glacial lakes are typical examples of
a. eutrophic lakes
b. hypereutrophic lakes
c. oligotrophic lakes
d. mesotrophic lakes
9 Which of these is not a climatic forcing for Earth?
a. changes in plate tectonics
b. changes in Earth's orbit
c. changes in Sun's orbit
d. changes in Sun's strength
10 Which of these is not a characteristic of fitness?
a. Fitness is environment-specific.
b. Fitness is species-specific.
c. Higher reproductive rate means higher fitness.
d. Fitness should be measured across several generations.

'''

lines = text.split("\n")
questions = []

for i in range(len(lines)):
    line = lines[i]
    if len(line) > 0 and line[0].isdigit():
        questions.append({
            "question": line[line.index(" "):].strip(),
            "options": [
                lines[i+1][2:].strip(),
                lines[i+2][2:].strip(),
                lines[i+3][2:].strip(),
                lines[i+4][2:].strip(),
            ],
            "correct": 0,
            "id": len(questions) + 1
        })

# export questions in json form
with open("questions.json", "w") as f:
    json.dump(questions, f, indent=4)

print(f"Number of questions: {len(questions)}\n")

# display random 10 questions from the above array
random.shuffle(questions)
for i in range(len(questions)):
    print(f"{i+1}. {questions[i]['question']}")
    for j in range(4):
        options = questions[i]["options"]
        random.shuffle(options)
        print(f"    {chr(j+97)}. {options[j]}")
    print()

print(questions)
