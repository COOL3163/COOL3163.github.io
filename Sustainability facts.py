#!/usr/bin/env python3

# This file contains facts and information about sustainability challenges in Hong Kong
# These facts are randomly displayed to the player during the game to enhance the educational value

HK_SUSTAINABILITY_FACTS = [
    # Waste Management
    "Hong Kong generates over 15,000 tonnes of municipal solid waste per day, with a recycling rate of only about 30%.",
    "Hong Kong's three main landfills are expected to reach capacity in the near future, creating an urgent waste management crisis.",
    "The waste charging scheme in Hong Kong aims to encourage waste reduction through a 'polluter pays' principle.",
    "Food waste accounts for about 30% of municipal solid waste in Hong Kong.",
    "The plastic recycling rate in Hong Kong is less than 10%, much lower than many other developed cities.",

    # Energy & Carbon Emissions
    "Buildings account for about 90% of electricity consumption in Hong Kong.",
    "Hong Kong's per capita carbon emissions are around 6.5 tonnes, higher than many other metropolitan areas.",
    "Hong Kong has set a target to achieve carbon neutrality by 2050.",
    "The majority of Hong Kong's electricity comes from fossil fuels, though there are plans to increase the use of natural gas and renewable energy.",
    "Due to Hong Kong's dense urban environment, solar energy adoption faces significant space constraints.",

    # Water Resources
    "About 70-80% of Hong Kong's water supply is imported from Dongjiang in mainland China.",
    "Hong Kong's water consumption per capita is higher than many other developed cities.",
    "Seawater is used for toilet flushing in many parts of Hong Kong, saving fresh water resources.",
    "Hong Kong experiences significant water leakage in its distribution system, with loss rates around 15%.",
    "Despite being surrounded by water, freshwater scarcity is a significant concern for Hong Kong.",

    # Urban Greening & Biodiversity
    "Despite being known for its dense urban environment, about 40% of Hong Kong's land area is designated as country parks and nature reserves.",
    "Hong Kong is home to over 3,300 species of plants, 570 species of birds, and numerous other wildlife despite its small size.",
    "Urban tree coverage in Hong Kong is lower than many other major cities, contributing to urban heat island effects.",
    "Hong Kong's Mai Po Nature Reserve is an internationally recognized wetland, crucial for migratory birds.",
    "Coral communities in Hong Kong waters face threats from pollution, development, and climate change.",

    # Air Quality
    "Hong Kong's air pollution often exceeds World Health Organization guidelines, especially for particulate matter and nitrogen dioxide.",
    "Vehicle emissions are a major contributor to roadside air pollution in Hong Kong.",
    "Cross-border air pollution from the Pearl River Delta region significantly affects Hong Kong's air quality.",
    "Air pollution in Hong Kong is estimated to cause thousands of premature deaths annually.",
    "Hong Kong has implemented an Air Quality Health Index to inform the public about health risks from air pollution.",

    # Transportation
    "Hong Kong has one of the world's highest rates of public transportation usage, with over 90% of daily trips made on public transport.",
    "The MTR system is one of the most profitable and efficient metro systems globally.",
    "Despite high public transport usage, traffic congestion remains a significant issue in Hong Kong.",
    "Hong Kong has been slow to adopt electric vehicles compared to some other developed regions.",
    "Walking in Hong Kong can be challenging due to urban design issues, despite the compact city layout.",

    # Climate Change Impacts
    "As a coastal city, Hong Kong is vulnerable to sea-level rise and increased storm surge from typhoons due to climate change.",
    "Hong Kong has experienced a warming trend, with the annual mean temperature rising at 0.13°C per decade from 1885 to 2020.",
    "Extreme weather events, including more intense typhoons, are expected to become more frequent due to climate change.",
    "The urban heat island effect in Hong Kong can cause the city center to be several degrees warmer than rural areas.",
    "Climate change may increase the risk of vector-borne diseases in Hong Kong."
]

# Facts specific to each location in the game
LOCATION_SPECIFIC_FACTS = {
    "home": [
        "Residential buildings account for about 20% of Hong Kong's total electricity consumption.",
        "Many older residential buildings in Hong Kong lack proper insulation, leading to energy inefficiency.",
        "A typical Hong Kong household generates about 1.5 kg of waste per day.",
        "Installing water-efficient fixtures can reduce a Hong Kong household's water consumption by up to 30%.",
        "Hong Kong's high-rise residential buildings provide opportunities for vertical greening to improve air quality and reduce urban heat."
    ],
    "work": [
        "Commercial buildings account for about 65% of Hong Kong's total electricity consumption.",
        "The Hong Kong Green Building Council promotes sustainable building practices in the commercial sector.",
        "Many Hong Kong companies are now publishing sustainability reports as part of their corporate social responsibility.",
        "The government offers tax incentives for energy-efficient commercial building equipment.",
        "Office waste paper is a significant recyclable resource in Hong Kong's commercial sector."
    ],
    "market": [
        "Wet markets are an important part of Hong Kong's food culture but generate significant food waste.",
        "Local farms produce less than 2% of vegetables consumed in Hong Kong, with most produce imported.",
        "Single-use plastic packaging is common in Hong Kong markets, contributing to plastic waste issues.",
        "Community-supported agriculture initiatives are growing in Hong Kong, connecting consumers directly with local farmers.",
        "Hong Kong imports over 90% of its food, creating a large carbon footprint from food transportation."
    ],
    "beach": [
        "Hong Kong has over 40 gazetted beaches, many of which face pollution from marine debris.",
        "Microplastics have been found in high concentrations on Hong Kong beaches and in local marine life.",
        "Beach clean-ups in Hong Kong collect tens of thousands of kilograms of waste annually.",
        "Cigarette butts are among the most common litter items found on Hong Kong beaches.",
        "Several Hong Kong beaches have received poor water quality ratings due to pollution."
    ],
    "park": [
        "Hong Kong's country parks cover about 40% of the territory's land area.",
        "Urban parks in Hong Kong play a crucial role in providing green space in the dense city environment.",
        "Hong Kong's country parks receive over 12 million visitors annually.",
        "Many of Hong Kong's urban parks were formerly areas of natural vegetation that have been heavily modified.",
        "Community gardens in Hong Kong help promote local food production and environmental education."
    ]
}

# Tips for sustainable living in Hong Kong
SUSTAINABILITY_TIPS = [
    "Bring your own shopping bag to avoid plastic bag fees and reduce waste in Hong Kong's landfills.",
    "Use a reusable water bottle instead of buying bottled water - Hong Kong tap water is safe to drink if filtered.",
    "Take advantage of Hong Kong's excellent public transport system instead of taxis to reduce your carbon footprint.",
    "When dining out in Hong Kong, bring your own reusable container for leftovers to reduce single-use packaging waste.",
    "Support local Hong Kong farms by purchasing locally grown produce at farmers' markets.",
    "Choose seafood wisely - use WWF Hong Kong's seafood guide to select sustainable options.",
    "Participate in local beach clean-ups organized regularly around Hong Kong's coastlines.",
    "Consider 'second-hand first' - Hong Kong has many thrift stores and online platforms for pre-loved items.",
    "Turn off the air conditioning when not needed - air conditioners account for about 30% of residential electricity use in Hong Kong.",
    "Separate your recyclables properly and use Hong Kong's recycling facilities - but be aware that not all materials put in recycling bins end up being recycled.",
    "Walk more - many areas in Hong Kong are very walkable despite the hilly terrain.",
    "Support local businesses that practice sustainability to encourage more green initiatives in Hong Kong.",
    "When hiking in Hong Kong's country parks, always take your trash with you and stay on designated trails.",
    "Consider joining a community garden project to grow your own food and connect with nature in the urban environment.",
    "Turn off unnecessary lights and unplug electronics when not in use to save energy."
]
