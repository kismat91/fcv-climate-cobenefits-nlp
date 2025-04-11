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


def extract_score_probabilities_and_scores(llm_output: str):
    """
    Extract scores and probabilities from the LLM output.
    """
    output = {}
    total_score = 0
    characteristic = None
    line_number = 0

    lines = llm_output.split('\n')
    for line in lines:
        line_number += 1
        # Match characteristic headers
        char_match = re.match(r'.*Characteristic \d+: (.+)', line)
        if char_match:
            characteristic = char_match.group(1).strip()
            output[characteristic] = []
            # question_index = 0
            continue
        
        # Match guiding question
        question_match = re.match(r'.*Guiding Question: (.+)', line)
        if question_match and characteristic:
            question = question_match.group(1).strip()
            output[characteristic].append({
                'question': question,
                'probabilities': {},
                'score': None
            })
            continue
        
        # Match probabilities line
        prob_match = re.match(r'.*score 0 \[(\d+(\.\d+)?)\], score 1 \[(\d+(\.\d+)?)\], score 2 \[(\d+(\.\d+)?)\], score 3 \[(\d+(\.\d+)?)\]', line)
        if prob_match and characteristic:
            probs = list(map(float, prob_match.groups()[::2]))
            probs_dict = {
                'score_0': probs[0],
                'score_1': probs[1],
                'score_2': probs[2],
                'score_3': probs[3],
            }

            # Get all indices (scores) with the maximum probability
            max_prob = max(probs)
            max_score = probs.index(max_prob)

            output[characteristic].append({'probabilities': probs_dict})
            output[characteristic][-1]['score'] = max_score
            total_score += max_score

    return output, total_score



# Example usage
if __name__ == "__main__":
    scores, total_score = extract_score_probabilities_and_scores(test_llm_output)
    print(json.dumps(scores, indent=4))
    print(f"Total Score: {total_score}")