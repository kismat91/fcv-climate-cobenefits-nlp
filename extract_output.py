import re
import json


test_llm_output = """"" \
### Characteristic 1: Consider How Interactions Between Climate & FCV Affect Program Delivery

#### Guiding Question: Does the PAD explicitly identify risks to project implementation from FCV-related barriers (e.g., security risks, institutional weaknesses, or strained community relations)?
**Analysis:** The PAD acknowledges potential risks related to institutional weaknesses and capacity constraints within local authorities. It highlights that Kandy and Galle have significantly weaker capacities compared to the Colombo Metropolitan Region, which could hinder effective project implementation. However, while it addresses some risks, it does not go into depth regarding security risks or strained community relations, limiting the understanding of FCV-related barriers.
**Score:** 2  
**Probabilities:** score 0 [0], score 1 [0.4], score 2 [0.6], score 3 [0]

#### Guiding Question: To what extent does the PAD seek to identify the specific pathways through which climate impacts interact with FCV dynamics?
**Analysis:** The PAD mentions that climate change impacts, such as increased rainfall intensity leading to flooding in Galle, are a significant concern. However, it does not delve into how these climatic factors may exacerbate existing FCV dynamics like community tensions or governance issues. The pathways of these interactions could be better articulated, leading to a moderate score.
**Score:** 2  
**Probabilities:** score 0 [0], score 1 [0.5], score 2 [0.5], score 3 [0]

---

### Characteristic 2: Mitigate the Risk of Climate Actions Resulting in Maladaptation

#### Guiding Question: Does the PAD incorporate specific safeguards to ensure project interventions do not exacerbate FCV-related vulnerabilities or create new sources of tension?
**Analysis:** The PAD includes a Social Management Framework and specifies that resettlement policies have been developed to minimize adverse social impacts. It emphasizes community participation, which is crucial in reducing tensions. However, while there are safeguards mentioned, it lacks specific strategies aimed at mitigating climate action-induced vulnerabilities comprehensively, resulting in a moderate response.
**Score:** 2  
**Probabilities:** score 0 [0], score 1 [0.3], score 2 [0.7], score 3 [0]

#### Guiding Question: To what extent are adaptive mechanisms embedded into the project to accommodate evolving FCV conditions in the country or region?
**Analysis:** The PAD does discuss adaptive mechanisms such as capacity building for local authorities and the establishment of PMUs in Kandy and Galle. These mechanisms suggest an awareness of the need to adapt to changing conditions, but the extent to which they address evolving FCV dynamics is not thoroughly explored. More detail on adaptive measures would strengthen this aspect.
**Score:** 2  
**Probabilities:** score 0 [0], score 1 [0.4], score 2 [0.6], score 3 [0]

#### Guiding Question: Does the PAD show evidence of explicit efforts to balance immediate needs with long-term resilience-building in a way that avoids maladaptive outcomes?
**Analysis:** The documentation reflects a commitment to balancing immediate urban service improvements with long-term urban planning goals, like developing integrated urban management plans. However, while it mentions the need for sustainable practices, explicit strategies to avoid maladaptive outcomes are less pronounced. 
**Score:** 2  
**Probabilities:** score 0 [0], score 1 [0.5], score 2 [0.5], score 3 [0]

---

### Characteristic 3: Prioritize Climate Actions That Address FCV Root Causes & Enhance Peacebuilding

#### Guiding Question: Does the PAD include interventions that explicitly address root causes of FCV, such as inequitable access to resources or weak governance?
**Analysis:** The PAD does discuss the importance of improving urban infrastructure, which can indirectly address some root causes of FCV like inequitable access to resources. However, it doesn't clearly articulate how interventions will specifically target these root issues, resulting in a moderate score.
**Score:** 2  
**Probabilities:** score 0 [0], score 1 [0.5], score 2 [0.5], score 3 [0]

#### Guiding Question: Does the project actively seek to promote peacebuilding, such as fostering trust, social cohesion, or conflict resolution?
**Analysis:** The PAD emphasizes community engagement and participation in decision-making processes, which can foster social cohesion. However, it does not present specific peacebuilding initiatives or programs aimed at resolving local conflicts that may arise from urban development activities, thus receiving a moderate score.
**Score:** 2  
**Probabilities:** score 0 [0], score 1 [0.4], score 2 [0.6], score 3 [0]

---

### Characteristic 4: Prioritize the Needs and Capacities of Vulnerable Regions and Groups

#### Guiding Question: Does the PAD explicitly identify vulnerable populations (e.g., women, displaced persons, minorities) and include measures to address their specific needs?
**Analysis:** The PAD acknowledges vulnerable populations and outlines plans for gender-sensitive approaches in the resettlement process, including targeted support for women-headed households. This inclusion demonstrates an effort to address the needs of vulnerable groups effectively.
**Score:** 3  
**Probabilities:** score 0 [0], score 1 [0], score 2 [0.2], score 3 [0.8]

#### Guiding Question: Are mechanisms included to ensure equitable benefit-sharing and avoid reinforcing inequalities?
**Analysis:** The PAD includes provisions to ensure that benefits from urban upgrades are equitably distributed among the affected populations and that the resettlement framework addresses potential inequalities. However, the mechanisms for monitoring and ensuring these benefits could be clearer and more robust.
**Score:** 2  
**Probabilities:** score 0 [0], score 1 [0.4], score 2 [0.5], score 3 [0.1]

---

### Characteristic 5: Encourage Coordination Across Development, DRM, & Peacebuilding Actors

#### Guiding Question: Does the PAD demonstrate evidence of active collaboration with stakeholders across sectors (e.g., humanitarian, peacebuilding, disaster risk management)?
**Analysis:** The PAD outlines the establishment of Steering and Coordination Committees that include various stakeholders from different sectors, indicating a structure for collaboration. However, the effectiveness and extent of this collaboration in practice remain somewhat vague and need further detail.
**Score:** 2  
**Probabilities:** score 0 [0], score 1 [0.5], score 2 [0.5], score 3 [0]

#### Guiding Question: Does the PAD outline mechanisms to align actions, resolve mandate overlaps, and avoid duplication across relevant actors?
**Analysis:** The document mentions coordination mechanisms among various project partners and agencies, but lacks specific actions or strategies to address potential overlaps or duplication. This aspect is important for ensuring cohesive implementation across development efforts, leading to a moderate score.
**Score:** 2  
**Probabilities:** score 0 [0], score 1 [0.4], score 2 [0.6], score 3 [0]

---

### Overall Summary:
The PAD for the Strategic Cities Development Project in Sri Lanka generally demonstrates a moderate sensitivity to FCV issues, particularly in identifying risks and addressing the needs of vulnerable populations. Strengths include a well-articulated social management framework and mechanisms for community engagement. However, it lacks comprehensive strategies that explicitly link climate impacts to FCV dynamics and could benefit from clearer frameworks for peacebuilding and conflict resolution. Overall, while the project addresses several critical aspects of FCV sensitivity, there is room for improvement in articulating detailed mechanisms and strategies to enhance resilience and minimize maladaptive outcomes.
"""

test_llm_output_2 = """\
Here is the evaluation of the Project Appraisal Document (PAD) based on the Fragility, Conflict, and Violence (FCV) Sensitivity Assessment Protocol.

### Characteristic 1: Consider How Interactions Between Climate & FCV Affect Program Delivery

**Guiding Question:** Does the PAD explicitly identify risks to project implementation from FCV-related barriers (e.g., security risks, institutional weaknesses, or strained community relations)?  
**Analysis:** The PAD identifies potential barriers to project implementation, particularly regarding involuntary resettlement due to land acquisition and mentions the sensitivity required in construction activities in prone areas. However, it does not comprehensively detail security risks or institutional weaknesses beyond the initial mention.  
**Probabilities:** score 0 [0.1], score 1 [0.3], score 2 [0.5], score 3 [0.1]

**Guiding Question:** To what extent does the PAD seek to identify the specific pathways through which climate impacts interact with FCV dynamics?  
**Analysis:** The PAD describes environmental assessments and mentions sustainability considerations but does not deeply explore the interconnected pathways between climate impacts and FCV dynamics.  
**Probabilities:** score 0 [0.2], score 1 [0.4], score 2 [0.3], score 3 [0.1]

### Characteristic 2: Mitigate the Risk of Climate Actions Resulting in Maladaptation

**Guiding Question:** Does the PAD incorporate specific safeguards to ensure project interventions do not exacerbate FCV-related vulnerabilities or create new sources of tension?  
**Analysis:** The PAD outlines a Social Management Framework (SMF) aimed at mitigating adverse social impacts, particularly from resettlement. There is an acknowledgment of the need for safeguards, but specific measures to avoid exacerbating FCV-related issues could be more detailed.  
**Probabilities:** score 0 [0.1], score 1 [0.2], score 2 [0.5], score 3 [0.2]

**Guiding Question:** To what extent are adaptive mechanisms embedded into the project to accommodate evolving FCV conditions in the country or region?  
**Analysis:** The PAD mentions monitoring and evaluation as part of implementation but does not explicitly outline adaptive mechanisms to respond to evolving FCV conditions, suggesting a gap.  
**Probabilities:** score 0 [0.3], score 1 [0.4], score 2 [0.2], score 3 [0.1]

**Guiding Question:** Does the PAD show evidence of explicit efforts to balance immediate needs with long-term resilience-building in a way that avoids maladaptive outcomes?  
**Analysis:** There is some mention of resilience and sustainability in the project design but lacking in specific strategies to balance immediate needs without risking maladaptive outcomes.  
**Probabilities:** score 0 [0.2], score 1 [0.3], score 2 [0.4], score 3 [0.1]

### Characteristic 3: Prioritize Climate Actions That Address FCV Root Causes & Enhance Peacebuilding

**Guiding Question:** Does the PAD include interventions that explicitly address root causes of FCV, such as inequitable access to resources or weak governance?  
**Analysis:** The PAD primarily focuses on infrastructural improvements rather than directly addressing root causes of FCV such as inequitable resource distribution. This is a notable gap.  
**Probabilities:** score 0 [0.3], score 1 [0.5], score 2 [0.2], score 3 [0.0]

**Guiding Question:** Does the project actively seek to promote peacebuilding, such as fostering trust, social cohesion, or conflict resolution?  
**Analysis:** There are references to community engagement, but the specific peacebuilding initiatives or strategies to foster social cohesion are not well articulated in the document.  
**Probabilities:** score 0 [0.4], score 1 [0.4], score 2 [0.2], score 3 [0.0]

### Characteristic 4: Prioritize the Needs and Capacities of Vulnerable Regions and Groups

**Guiding Question:** Does the PAD explicitly identify vulnerable populations (e.g., women, displaced persons, minorities) and include measures to address their specific needs?  
**Analysis:** The PAD mentions affected communities due to land acquisition but lacks in-depth analysis or specific measures tailored for vulnerable populations within those communities.  
**Probabilities:** score 0 [0.2], score 1 [0.5], score 2 [0.2], score 3 [0.1]

**Guiding Question:** Are mechanisms included to ensure equitable benefit-sharing and avoid reinforcing inequalities?  
**Analysis:** The document does outline a framework for compensation and rehabilitation but does not comprehensively address mechanisms for equitable benefit-sharing, which is needed for ensuring fairness.  
**Probabilities:** score 0 [0.2], score 1 [0.4], score 2 [0.3], score 3 [0.1]

### Characteristic 5: Encourage Coordination Across Development, DRM, & Peacebuilding Actors

**Guiding Question:** Does the PAD demonstrate evidence of active collaboration with stakeholders across sectors (e.g., humanitarian, peacebuilding, disaster risk management)?  
**Analysis:** The PAD indicates stakeholder consultations and aligns with some collaborative frameworks but lacks extensive detail on specific partnerships across sectors related to peacebuilding or disaster risk management (DRM).  
**Probabilities:** score 0 [0.3], score 1 [0.4], score 2 [0.2], score 3 [0.1]

**Guiding Question:** Does the PAD outline mechanisms to align actions, resolve mandate overlaps, and avoid duplication across relevant actors?  
**Analysis:** The PAD lacks clarity on specific mechanisms for coordinating actions among different actors, which is crucial for effective implementation and avoiding duplication of efforts.  
**Probabilities:** score 0 [0.4], score 1 [0.4], score 2 [0.1], score 3 [0.1]

### Overall Summary:
The PAD shows a moderate effort to address FCV sensitivity issues, particularly in terms of social impacts and mitigation measures. However, significant gaps remain in explicitly identifying risks related to climate impacts and FCV dynamics, deeply addressing root causes, and ensuring collaboration across actors. The document could significantly benefit from a more thorough analysis and explicit measures to enhance resilience and social cohesion among vulnerable populations.

---
🧮 **Usage Summary**
- Input tokens: 7591
- Output tokens: 1381
- 💰 Estimated cost: $0.05867
"""

# test_llm_output_3 = """\
# ### Characteristic 1: Consider How Interactions Between Climate & FCV Affect Program Delivery

# #### Guiding Question: Does the PAD explicitly identify risks to project implementation from FCV-related barriers (e.g., security risks, institutional weaknesses, or strained community relations)?
# **Analysis:** The PAD identifies various risks related to project implementation, including institutional weaknesses and fragmentation of responsibilities among multiple agencies. It acknowledges the challenges posed by the relatively weak capacity of local authorities in Kandy and Galle, which could impact the project's success. However, it lacks a thorough exploration of specific security risks and community relations issues that could hinder implementation. 
# **Score:** 2
# **Probabilities:** 
# - score 0 [0], score 1 [0.2], score 2 [0.6], score 3 [0.2]

# #### Guiding Question: To what extent does the PAD seek to identify the specific pathways through which climate impacts interact with FCV dynamics?
# **Analysis:** The PAD mentions the impact of climate change on flooding in Galle, acknowledging increased rainfall intensity. However, it does not delve deeply into how these climate impacts create or exacerbate existing FCV dynamics within the project regions. There's a need for more explicit connections drawn between climate impacts and potential conflict or violence scenarios.
# **Score:** 1
# **Probabilities:** 
# - score 0 [0], score 1 [0.7], score 2 [0.3]

# ### Characteristic 2: Mitigate the Risk of Climate Actions Resulting in Maladaptation

# #### Guiding Question: Does the PAD incorporate specific safeguards to ensure project interventions do not exacerbate FCV-related vulnerabilities or create new sources of tension?
# **Analysis:** The PAD outlines various safeguards, including a Resettlement Policy Framework and Environmental Assessment and Management Framework. It indicates that steps will be taken to mitigate adverse impacts on local communities. However, it does not provide detailed measures aimed directly at avoiding exacerbation of FCV-related vulnerabilities.
# **Score:** 2
# **Probabilities:** 
# - score 0 [0], score 1 [0.1], score 2 [0.8], score 3 [0.1]

# #### Guiding Question: To what extent are adaptive mechanisms embedded into the project to accommodate evolving FCV conditions in the country or region?
# **Analysis:** The PAD outlines institutional strengthening and capacity-building components aimed at enhancing the abilities of local agencies to deal with emerging challenges. However, it lacks detailed mechanisms or adaptive strategies specifically tailored to changing FCV conditions as they evolve during implementation. 
# **Score:** 1
# **Probabilities:** 
# - score 0 [0], score 1 [0.5], score 2 [0.5]

# #### Guiding Question: Does the PAD show evidence of explicit efforts to balance immediate needs with long-term resilience-building in a way that avoids maladaptive outcomes?
# **Analysis:** The PAD mentions improvements to urban infrastructure that would contribute to long-term resilience, but it doesn't explicitly articulate a balanced approach between immediate interventions and long-term resilience planning. There is a lack of clear indicators that address how immediate needs will be effectively balanced with sustainable development goals.
# **Score:** 1
# **Probabilities:** 
# - score 0 [0], score 1 [0.6], score 2 [0.4]

# ### Characteristic 3: Prioritize Climate Actions That Address FCV Root Causes & Enhance Peacebuilding

# #### Guiding Question: Does the PAD include interventions that explicitly address root causes of FCV, such as inequitable access to resources or weak governance?
# **Analysis:** The PAD highlights the need for improved governance and equitable access to urban services but does not explicitly link these to identified root causes of FCV. The language suggests awareness, but there are no direct interventions aimed at addressing these root causes, such as resource allocation strategies or community engagement frameworks.
# **Score:** 1
# **Probabilities:** 
# - score 0 [0], score 1 [0.7], score 2 [0.3]

# #### Guiding Question: Does the project actively seek to promote peacebuilding, such as fostering trust, social cohesion, or conflict resolution?
# **Analysis:** The PAD discusses the importance of social cohesion and community engagement but lacks concrete peacebuilding strategies or approaches that facilitate trust-building among communities affected by the project. The potential for conflict resolution mechanisms to be integrated into the project remains underexplored.
# **Score:** 1
# **Probabilities:** 
# - score 0 [0], score 1 [0.8], score 2 [0.2]

# ### Characteristic 4: Prioritize the Needs and Capacities of Vulnerable Regions and Groups

# #### Guiding Question: Does the PAD explicitly identify vulnerable populations (e.g., women, displaced persons, minorities) and include measures to address their specific needs?
# **Analysis:** The PAD acknowledges the presence of vulnerable populations and proposes a gender strategy that aims to support impacted groups, such as women and displaced households. However, it lacks detailed plans or measures explicitly targeting these groups within the project design.
# **Score:** 2
# **Probabilities:** 
# - score 0 [0], score 1 [0.2], score 2 [0.7], score 3 [0.1]

# #### Guiding Question: Are mechanisms included to ensure equitable benefit-sharing and avoid reinforcing inequalities?
# **Analysis:** The PAD outlines a framework for equitable benefit-sharing and addresses potential social impacts, but it is vague on how these mechanisms will be implemented and monitored throughout the project lifecycle. More clarity and detail are needed.
# **Score:** 1
# **Probabilities:** 
# - score 0 [0], score 1 [0.5], score 2 [0.5]

# ### Characteristic 5: Encourage Coordination Across Development, DRM, & Peacebuilding Actors

# #### Guiding Question: Does the PAD demonstrate evidence of active collaboration with stakeholders across sectors (e.g., humanitarian, peacebuilding, disaster risk management)?
# **Analysis:** The PAD describes the establishment of a Steering Committee and Coordination and Consultative Committees aimed at inter-agency collaboration. However, it does not provide details on how other sectors, such as humanitarian and peacebuilding actors, are integrated into these collaborative efforts.
# **Score:** 2
# **Probabilities:** 
# - score 0 [0], score 1 [0.1], score 2 [0.8], score 3 [0.1]

# #### Guiding Question: Does the PAD outline mechanisms to align actions, resolve mandate overlaps, and avoid duplication across relevant actors?
# **Analysis:** The PAD mentions the establishment of structures to facilitate inter-agency coordination and has identified relevant agencies to avoid overlaps. However, it lacks specific mechanisms that outline how conflicts in mandates will be resolved and how duplication will be actively managed.
# **Score:** 1
# **Probabilities:** 
# - score 0 [0], score 1 [0.6], score 2 [0.4]

# ### Overall Summary:
# The PAD demonstrates a moderate level of awareness regarding FCV sensitivity but lacks depth in several areas, particularly in explicitly linking climate impacts to FCV dynamics, detailing adaptive mechanisms, and providing concrete peacebuilding initiatives. While some safeguards and frameworks are established to address vulnerabilities and promote equity, the document could benefit from a stronger focus on identifying and addressing the root causes of FCV, along with more explicit strategies for engaging vulnerable populations and fostering coordination across relevant sectors. Overall, the PAD shows commitment but needs significant enhancement in specificity and breadth of FCV-sensitive measures.
# """

test_llm_output_4 = """\
### Evaluation of the Project Appraisal Document (PAD) for the Sri Lanka Strategic Cities Development Project

---

### Characteristic 1: Consider How Interactions Between Climate & FCV Affect Program Delivery

**Guiding Question 1:** Does the PAD explicitly identify risks to project implementation from FCV-related barriers (e.g., security risks, institutional weaknesses, or strained community relations)?  
**Analysis:** The PAD acknowledges several challenges that may affect project implementation, including inadequate urban services and infrastructure, institutional fragmentation, and the necessity for integrated planning. However, it does not sufficiently address specific FCV-related barriers such as security risks and community relations. The mention of "capacity risks" at the local level is vague and does not delve into potential conflict implications or community tensions directly arising from these weaknesses.  
**Probabilities:** score 0 [0.1], score 1 [0.4], score 2 [0.4], score 3 [0.1]

**Guiding Question 2:** To what extent does the PAD seek to identify the specific pathways through which climate impacts interact with FCV dynamics?  
**Analysis:** The PAD identifies climate change as a factor that influences urban infrastructure, particularly regarding flooding concerns in Galle. However, it does not comprehensively discuss the interaction between climate impacts and FCV dynamics, especially how these may exacerbate existing vulnerabilities or lead to conflicts. There is a lack of thorough analytics concerning how climate change could heighten fragility or tensions in the affected urban areas.  
**Probabilities:** score 0 [0.2], score 1 [0.4], score 2 [0.3], score 3 [0.1]

---

### Characteristic 2: Mitigate the Risk of Climate Actions Resulting in Maladaptation

**Guiding Question 1:** Does the PAD incorporate specific safeguards to ensure project interventions do not exacerbate FCV-related vulnerabilities or create new sources of tension?  
**Analysis:** While the PAD discusses a Social Management Framework (SMF) and Resettlement Action Framework (RAP) to manage social impacts, it lacks specific safeguards that directly address FCV vulnerabilities related to tensions or conflicts arising from project interventions. The measures mentioned are more focused on environmental and social impacts rather than on FCV-related issues.  
**Probabilities:** score 0 [0.2], score 1 [0.5], score 2 [0.2], score 3 [0.1]

**Guiding Question 2:** To what extent are adaptive mechanisms embedded into the project to accommodate evolving FCV conditions in the country or region?  
**Analysis:** The PAD does mention the establishment of a PMU with local offices and intends to build capacities of local municipalities. However, the adaptability of these mechanisms to evolving FCV conditions remains unclear. There is no discussion on how the project will adjust to changing dynamics in conflict or fragility over time.  
**Probabilities:** score 0 [0.3], score 1 [0.5], score 2 [0.2], score 3 [0.0]

**Guiding Question 3:** Does the PAD show evidence of explicit efforts to balance immediate needs with long-term resilience-building in a way that avoids maladaptive outcomes?  
**Analysis:** The project is primarily focused on immediate urban service improvements without a robust strategy for balancing these with long-term resilience measures. The PAD lacks a clear framework that ties short-term interventions to long-term resilience, particularly in the context of FCV dynamics.  
**Probabilities:** score 0 [0.3], score 1 [0.4], score 2 [0.2], score 3 [0.1]

---

### Characteristic 3: Prioritize Climate Actions That Address FCV Root Causes & Enhance Peacebuilding

**Guiding Question 1:** Does the PAD include interventions that explicitly address root causes of FCV, such as inequitable access to resources or weak governance?  
**Analysis:** While the PAD recognizes the need for improved urban services and infrastructure, it does not address the root causes of FCV effectively, such as inequitable access to resources or governance issues. The considerations for equitable resource distribution are missing, which is crucial in a post-conflict context.  
**Probabilities:** score 0 [0.2], score 1 [0.5], score 2 [0.2], score 3 [0.1]

**Guiding Question 2:** Does the project actively seek to promote peacebuilding, such as fostering trust, social cohesion, or conflict resolution?  
**Analysis:** There are vague references to fostering social cohesion through urban improvements; however, there’s no explicit strategy or concrete interventions aimed at peacebuilding and conflict resolution. The overall approach appears more focused on infrastructure than on addressing social dynamics and relationships within communities.  
**Probabilities:** score 0 [0.3], score 1 [0.4], score 2 [0.2], score 3 [0.1]

---

### Characteristic 4: Prioritize the Needs and Capacities of Vulnerable Regions and Groups

**Guiding Question 1:** Does the PAD explicitly identify vulnerable populations (e.g., women, displaced persons, minorities) and include measures to address their specific needs?  
**Analysis:** The PAD acknowledges the need for social assessments and mentions gender considerations; however, it does not sufficiently identify specific vulnerable groups or their needs in detail. The measures provided are generic and lack specificity on how they will be applied to these groups.  
**Probabilities:** score 0 [0.2], score 1 [0.5], score 2 [0.2], score 3 [0.1]

**Guiding Question 2:** Are mechanisms included to ensure equitable benefit-sharing and avoid reinforcing inequalities?  
**Analysis:** The PAD mentions a Social Management Framework that aims to address social equity; however, it lacks concrete mechanisms for ensuring that benefits are shared equitably. The general references do not provide a strong assurance against the potential reinforcement of existing inequalities.  
**Probabilities:** score 0 [0.3], score 1 [0.4], score 2 [0.2], score 3 [0.1]

---

### Characteristic 5: Encourage Coordination Across Development, DRM, & Peacebuilding Actors

**Guiding Question 1:** Does the PAD demonstrate evidence of active collaboration with stakeholders across sectors (e.g., humanitarian, peacebuilding, disaster risk management)?  
**Analysis:** The PAD outlines a Steering Committee structure intended to facilitate inter-agency collaboration; however, evidence of active collaboration across sectors is limited. While there is a mention of the need for coordination, specifics on how this will be achieved, especially with stakeholders from humanitarian and peacebuilding sectors, are lacking.  
**Probabilities:** score 0 [0.3], score 1 [0.4], score 2 [0.2], score 3 [0.1]

**Guiding Question 2:** Does the PAD outline mechanisms to align actions, resolve mandate overlaps, and avoid duplication across relevant actors?  
**Analysis:** The PAD details the establishment of a Steering Committee to address some coordination challenges; however, it does not provide a thorough mechanism for resolving mandate overlaps or ensuring that actions of various actors are aligned. It appears to rely on existing structures without addressing potential gaps.  
**Probabilities:** score 0 [0.3], score 1 [0.4], score 2 [0.2], score 3 [0.1]

---

### Overall Summary:

The Project Appraisal Document for the Sri Lanka Strategic Cities Development Project has several strengths, particularly in its recognition of the importance of urban infrastructure and service improvements in post-conflict settings. However, it falls short in addressing the complexities and sensitivities associated with fragility, conflict, and violence (FCV). The document lacks thorough analyses and explicit strategies to address FCV-related barriers, root causes, and the needs of vulnerable populations. Coordination among various stakeholders is outlined but lacks depth, and mechanisms to ensure equitable benefit-sharing are minimal. Overall, while the PAD lays a foundation for urban development, it requires more robust integration of FCV sensitivity assessments to ensure long-term sustainability and peacebuilding in the affected regions.
"""

test_llm_output_5 = """\
Here's an evaluation of the Project Appraisal Document (PAD) based on the FCV-Sensitivity Assessment Protocol:

### Characteristic 1: Consider How Interactions Between Climate & FCV Affect Program Delivery

**Guiding Question:** Does the PAD explicitly identify risks to project implementation from FCV-related barriers (e.g., security risks, institutional weaknesses, or strained community relations)?  
**Analysis:** The PAD highlights potential risks such as governance issues and capacity weaknesses in local municipalities, which may hinder project implementation. It acknowledges that political and social tensions could arise from local governance challenges. However, the identification of these risks is somewhat general, lacking specific examples or scenarios.  
**Probabilities:** score 0 [0.1], score 1 [0.3], score 2 [0.4], score 3 [0.2]

**Guiding Question:** To what extent does the PAD seek to identify the specific pathways through which climate impacts interact with FCV dynamics?  
**Analysis:** The analysis of the interaction pathways is limited. Although some mention of climate impacts exists, overall, it does not sufficiently explore how these impacts exacerbate FCV issues. A detailed examination into the cause-and-effect relationships is absent, leading to a lower score.  
**Probabilities:** score 0 [0.2], score 1 [0.4], score 2 [0.3], score 3 [0.1]

---

### Characteristic 2: Mitigate the Risk of Climate Actions Resulting in Maladaptation

**Guiding Question:** Does the PAD incorporate specific safeguards to ensure project interventions do not exacerbate FCV-related vulnerabilities or create new sources of tension?  
**Analysis:** The document indicates the development of a Social Management Framework (SMF) to address adverse social impacts, which includes provisions for involuntary resettlement. Nevertheless, it does not present concrete safeguards that directly prevent exacerbation of FCV vulnerabilities.  
**Probabilities:** score 0 [0.2], score 1 [0.3], score 2 [0.4], score 3 [0.1]

**Guiding Question:** To what extent are adaptive mechanisms embedded into the project to accommodate evolving FCV conditions in the country or region?  
**Analysis:** The document mentions the need to build capacity in local authorities and support adaptive management but lacks detailed mechanisms for how the project will evolve with changes in FCV conditions post-implementation.  
**Probabilities:** score 0 [0.3], score 1 [0.5], score 2 [0.2], score 3 [0.0]

**Guiding Question:** Does the PAD show evidence of explicit efforts to balance immediate needs with long-term resilience-building in a way that avoids maladaptive outcomes?  
**Analysis:** While the PAD recognizes the importance of sustainability and long-term environmental improvements, detailed strategies for balancing these against immediate needs are insufficiently developed.  
**Probabilities:** score 0 [0.2], score 1 [0.3], score 2 [0.4], score 3 [0.1]

---

### Characteristic 3: Prioritize Climate Actions That Address FCV Root Causes & Enhance Peacebuilding

**Guiding Question:** Does the PAD include interventions that explicitly address root causes of FCV, such as inequitable access to resources or weak governance?  
**Analysis:** The PAD acknowledges governance weaknesses but does not explicitly outline interventions directly targeting these root causes. The focus on social equity is implied but not elaborated.  
**Probabilities:** score 0 [0.2], score 1 [0.4], score 2 [0.3], score 3 [0.1]

**Guiding Question:** Does the project actively seek to promote peacebuilding, such as fostering trust, social cohesion, or conflict resolution?  
**Analysis:** While some community-focused interventions are mentioned, the PAD lacks a clear, coherent strategy aimed specifically at peacebuilding or fostering social cohesion in conflict-prone areas.   
**Probabilities:** score 0 [0.3], score 1 [0.5], score 2 [0.2], score 3 [0.0]

---

### Characteristic 4: Prioritize the Needs and Capacities of Vulnerable Regions and Groups

**Guiding Question:** Does the PAD explicitly identify vulnerable populations (e.g., women, displaced persons, minorities) and include measures to address their specific needs?  
**Analysis:** The document notes the existence of a Social Assessment but does not adequately identify specific vulnerable populations or detail measures designed for their support.  
**Probabilities:** score 0 [0.1], score 1 [0.6], score 2 [0.3], score 3 [0.0]

**Guiding Question:** Are mechanisms included to ensure equitable benefit-sharing and avoid reinforcing inequalities?  
**Analysis:** Although the PAD includes some mechanism for compensation regarding involuntary displacement, it lacks comprehensive strategies for ensuring equitable benefit-sharing across diverse community groups.  
**Probabilities:** score 0 [0.3], score 1 [0.4], score 2 [0.2], score 3 [0.1]

---

### Characteristic 5: Encourage Coordination Across Development, DRM, & Peacebuilding Actors

**Guiding Question:** Does the PAD demonstrate evidence of active collaboration with stakeholders across sectors (e.g., humanitarian, peacebuilding, disaster risk management)?  
**Analysis:** The establishment of a Project Coordination and Consultative Committee indicates some effort towards stakeholder engagement, though details on collaborative strategies and outcomes are limited.  
**Probabilities:** score 0 [0.2], score 1 [0.3], score 2 [0.4], score 3 [0.1]

**Guiding Question:** Does the PAD outline mechanisms to align actions, resolve mandate overlaps, and avoid duplication across relevant actors?  
**Analysis:** The PAD mentions institutional arrangements but does not offer concrete mechanisms to actively align actions among varied stakeholders, leading to potential issues in coordination.  
**Probabilities:** score 0 [0.3], score 1 [0.5], score 2 [0.2], score 3 [0.0]

---

### Overall Summary
The PAD demonstrates some awareness of FCV sensitivity, particularly through the recognition of risks and the establishment of frameworks for social management and stakeholder coordination. However, it lacks specific strategies for addressing root causes of FCV, and opportunities for adaptive management based on evolving conditions are not thoroughly explored. The need for enhanced detail on vulnerable populations and collaborative mechanisms is evident, hampering its effectiveness in addressing FCV sensitivities comprehensively. Overall, while the PAD has merits, it requires substantial improvements to meet FCV-sensitive standards effectively.

---
🧮 **Usage Summary**
- Input tokens: 8027
- Output tokens: 1404
- 💰 Estimated cost: $0.06119
"""

test_llm_output_6 = """\
### Evaluation of the Project Appraisal Document (PAD) on FCV Sensitivity

**Characteristic 1: Consider How Interactions Between Climate & FCV Affect Program Delivery**

- **Guiding Question: Does the PAD explicitly identify risks to project implementation from FCV-related barriers (e.g., security risks, institutional weaknesses, or strained community relations)?**
  - **Analysis:** The PAD does mention various barriers to effective implementation, including the risks of social unrest and governance challenges stemming from Nepal's history of conflict. It recognizes the need for coordinated inter-agency efforts due to institutional weaknesses. However, it lacks explicit details on specific security risks or community relations issues that could impact project delivery.
  - **Probabilities:** score 0 [0.1], score 1 [0.4], score 2 [0.4], score 3 [0.1]

- **Guiding Question: To what extent does the PAD seek to identify the specific pathways through which climate impacts interact with FCV dynamics?**
  - **Analysis:** The document does not sufficiently delve into the pathways linking climate impacts with FCV dynamics, focusing instead on health and nutrition without adequately addressing how climate change might exacerbate existing vulnerabilities or conflicts.
  - **Probabilities:** score 0 [0.2], score 1 [0.5], score 2 [0.2], score 3 [0.1]

**Characteristic 2: Mitigate the Risk of Climate Actions Resulting in Maladaptation**

- **Guiding Question: Does the PAD incorporate specific safeguards to ensure project interventions do not exacerbate FCV-related vulnerabilities or create new sources of tension?**
  - **Analysis:** While the PAD outlines various interventions aimed at improving nutrition and health, it fails to detail specific safeguards or mitigation strategies to address potential tensions arising from resource competition or community divides.
  - **Probabilities:** score 0 [0.3], score 1 [0.5], score 2 [0.2], score 3 [0.0]

- **Guiding Question: To what extent are adaptive mechanisms embedded into the project to accommodate evolving FCV conditions in the country or region?**
  - **Analysis:** The document mentions periodic assessments and a learning framework, which indicates some level of adaptability. However, it does not robustly outline how these mechanisms will specifically respond to changing FCV conditions or climate impacts.
  - **Probabilities:** score 0 [0.2], score 1 [0.4], score 2 [0.3], score 3 [0.1]

- **Guiding Question: Does the PAD show evidence of explicit efforts to balance immediate needs with long-term resilience-building in a way that avoids maladaptive outcomes?**
  - **Analysis:** The PAD presents a focus on immediate nutrition needs but lacks a clear strategy for long-term resilience-building in the context of FCV sensitivity. There is a need for a more integrated approach that combines immediate interventions with sustainable development practices.
  - **Probabilities:** score 0 [0.3], score 1 [0.4], score 2 [0.2], score 3 [0.1]

**Characteristic 3: Prioritize Climate Actions That Address FCV Root Causes & Enhance Peacebuilding**

- **Guiding Question: Does the PAD include interventions that explicitly address root causes of FCV, such as inequitable access to resources or weak governance?**
  - **Analysis:** The PAD identifies some social determinants impacting nutrition, such as gender disparities and lack of education among women. However, it does not sufficiently explore how these factors are interlinked with broader governance and resource allocation issues.
  - **Probabilities:** score 0 [0.2], score 1 [0.4], score 2 [0.3], score 3 [0.1]

- **Guiding Question: Does the project actively seek to promote peacebuilding, such as fostering trust, social cohesion, or conflict resolution?**
  - **Analysis:** The project suggests community mobilization and involvement of various stakeholders, which could foster social cohesion. However, there are no explicit mechanisms for peacebuilding or conflict resolution outlined in the PAD.
  - **Probabilities:** score 0 [0.3], score 1 [0.4], score 2 [0.2], score 3 [0.1]

**Characteristic 4: Prioritize the Needs and Capacities of Vulnerable Regions and Groups**

- **Guiding Question: Does the PAD explicitly identify vulnerable populations (e.g., women, displaced persons, minorities) and include measures to address their specific needs?**
  - **Analysis:** The PAD does a commendable job of identifying vulnerable populations, particularly women and children. It outlines some tailored interventions, but lacks comprehensive measures specific to the diverse vulnerabilities within those groups.
  - **Probabilities:** score 0 [0.2], score 1 [0.3], score 2 [0.4], score 3 [0.1]

- **Guiding Question: Are mechanisms included to ensure equitable benefit-sharing and avoid reinforcing inequalities?**
  - **Analysis:** Although the PAD mentions the need for equitable access to resources, it does not adequately detail mechanisms to ensure that all groups benefit equitably from interventions, which is critical in a diverse and stratified social landscape.
  - **Probabilities:** score 0 [0.3], score 1 [0.4], score 2 [0.2], score 3 [0.1]

**Characteristic 5: Encourage Coordination Across Development, DRM, & Peacebuilding Actors**

- **Guiding Question: Does the PAD demonstrate evidence of active collaboration with stakeholders across sectors (e.g., humanitarian, peacebuilding, disaster risk management)?**
  - **Analysis:** The PAD indicates some level of collaboration among various sectors but falls short of demonstrating a cohesive strategy for incorporating peacebuilding and disaster risk management actors effectively into the project design.
  - **Probabilities:** score 0 [0.3], score 1 [0.4], score 2 [0.2], score 3 [0.1]

- **Guiding Question: Does the PAD outline mechanisms to align actions, resolve mandate overlaps, and avoid duplication across relevant actors?**
  - **Analysis:** The document mentions coordination mechanisms but lacks specific details on how to align actions among different actors or resolve overlaps in mandates, which are crucial for effective implementation.
  - **Probabilities:** score 0 [0.3], score 1 [0.5], score 2 [0.2], score 3 [0.0]

### Overall Summary
The PAD for the Sunaula Hazar Din - Community Action for Nutrition Project exhibits strengths in identifying vulnerable populations and outlining interventions aimed at improving nutrition. However, it falls short in addressing the complex interplay of fragility, conflict, and violence in the Nepalese context. Key gaps include a lack of explicit safeguards against FCV-related risks, insufficient attention to the dynamics of climate impacts, and a need for stronger mechanisms to ensure equitable benefit-sharing and promote peacebuilding initiatives. Enhanced focus on these areas would significantly improve the project's sensitivity to FCV issues and its potential for sustainable impact.
"""

def extract_report_content(llm_output: str):
    """
    Extract scores and probabilities from the LLM output.
    """
    output = {}
    total_score = 0
    characteristic = None
    current_question = None
    overall_summary = None

    lines = llm_output.split('\n')
    for i, line in enumerate(lines):
        # Match characteristic headers
        char_match = re.match(r'.*Characteristic \d+: (.+)', line)
        if char_match:
            characteristic = char_match.group(1).strip()
            output[characteristic] = []
            continue
        
        # Match guiding question
        question_match = re.match(r'.*Guiding Question(.+)', line)
        if question_match and characteristic:
            current_question = question_match.group(1).strip()
            output[characteristic].append({
                'question': current_question,
                'analysis': None,
                'probabilities': {},
                'score': None
            })
            continue
        
        # Match analysis line
        analysis_match = re.match(r'.*Analysis(.+)', line)
        if analysis_match and characteristic and current_question:
            analysis = analysis_match.group(1).strip()
            if output[characteristic]:
                output[characteristic][-1]['analysis'] = analysis
            continue
        
        # Match probabilities line
        prob_match = re.match(r'.*score 0 \[(\d+(\.\d+)?)\], score 1 \[(\d+(\.\d+)?)\], score 2 \[(\d+(\.\d+)?)\], score 3 \[(\d+(\.\d+)?)\]', line)
        if prob_match and characteristic and current_question:
            probs = list(map(float, prob_match.groups()[::2]))
            probs_dict = {
                'score_0': probs[0],
                'score_1': probs[1],
                'score_2': probs[2],
                'score_3': probs[3],
            }

            # Get all indices (scores) with the maximum probability
            #max_prob = max(probs)
            #max_score = probs.index(max_prob)

            #output[characteristic][-1]['probabilities'] = probs_dict
            #output[characteristic][-1]['score'] = max_score
            #total_score += max_score
            #continue

            sorted_probs = sorted(enumerate(probs), key=lambda x: x[1], reverse=True)
            (score1, prob1), (score2, prob2) = sorted_probs[:2]
            if abs(prob1 - prob2) <= 0.10:
                final_score = (score1 + score2) / 2
            else:
                final_score = score1

            output[characteristic][-1]['probabilities'] = probs_dict
            output[characteristic][-1]['score'] = final_score
            total_score += final_score


        # Match overall summary (on the same line or subsequent lines)
        if "Overall Summary" in line:
            summary_line = line.split("Overall Summary", 1)[1].strip(":").strip()
            if summary_line:
                overall_summary = summary_line
            else:
                # Check the next line(s) for the summary
                for j in range(i + 1, len(lines)):
                    next_line = lines[j].strip()
                    if next_line:
                        overall_summary = next_line
                        break

    # Combine total_score and overall_summary into a single dictionary
    summary = {
        "total_score": total_score,
        "overall_summary": overall_summary
    }

    return output, summary



# Example usage
if __name__ == "__main__":
    scores, summary = extract_report_content(test_llm_output_6)
    print(json.dumps(scores, indent=4))
    print(f"Total Score: {summary['total_score']}")
    print(f"Overall Summary: {summary['overall_summary']}")