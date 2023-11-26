
def freq_words():
    #str=input("Enter string: ")
    
    str2="""Your Highnesses,
        Excellencies,
        Namaskar!
        I express my gratitude to all of you for accepting my invitation and joining this summit today. On behalf of 140 crore Indians, you all are heartily welcomed.
        Friends,
        I remember the moment when my friend, the President of Indonesia, Joko Widodo, handed me the ceremonial gavel on November 16 last year. At that time, I had said that together we will make the G20 inclusive, ambiguous, action-oriented and decisive. Over the past year, together we have realized that vision. Together we have taken G-20 to new heights.
        Amidst a world fraught with distrust and challenges, it is mutual trust that binds us, connects us to each other.
        In this one year, we have believed in "One Earth, One Family, One Future". And, we have shown unity and cooperation beyond controversies.
        I can never forget that moment when all of us in Delhi unanimously welcomed the African Union to the G-20.
        The message of inclusivity that G-20 has given to the whole world is unprecedented. v It is a matter of pride for India that Africa has got a voice during its Presidency.
        In this one year, the whole world has also heard the echo of the Global South in G-20.
        In the Voice of Global South Summit last week, about 130 countries have wholeheartedly appreciated the decisions taken at the New Delhi G-20 Summit.
        The G-20 has emphasized the adoption of a human-centric approach while supporting innovation and digital technology. The G-20 has renewed faith in multilateralism.
        Together we have given direction to multilateral development banks and global governance reforms.
        And along with these, during the Presidency of India, G-20 has got the recognition of People's 20.
        Crores of ordinary citizens of India joined G-20, and celebrated it as a festival.
        Your Highnesses,
        Excellencies,
        When I had proposed this virtual summit, there was no forecast of what the global situation would be today. Recent months have brought forth new challenges. The insecurity and instability in the West Asia region, concerns us all. Our coming together today is a sign that we are sensitive to all these issues and stand together to resolve them.
        We believe that terrorism is unacceptable to all of us.
        The death of civilians, wherever they may be, is condemnable.
        We welcome the news of the release of hostages today, and hope for the swift release of all hostages. Ensuring the timely and continuous delivery of humanitarian aid is imperative. It is also crucial to ensure that the conflict between Israel and Hamas, does not take on any kind of regional form.
        The clouds of crises that we are witnessing today, as One Family, we possess the strength to work towards peace.
        From the point of view of human welfare, we can strengthen our voice against terror and violence, and for humanity.
        Today, India is prepared to walk together shoulder to shoulder, to meet the expectations of the world and of humanity.
        Friends,
        The 21st century world will have to give top priority to the concerns of the Global South moving forward.
        The countries of the Global South are going through many difficulties for which they are not responsible.
        In this context, the need of the hour is to give our full support to the development agenda.
        It is important that reforms are brought in the global economic and governance structures to make them bigger, better, effective, representative and future ready.
        Ensuring timely and affordable assistance to countries in need. Implement the action plan adopted to accelerate the 2030 Sustainable Development Goals.
        Friends,
        Our Aspirational District Program stands as a notable example of progress in the SDGs at the local level in India. I invite the G-20 countries and the Global South to examine the Aspirational District Programme, and witness the transformative impact it has had on the lives of 25 crore people in India.
        Friends,
        At the New Delhi Summit, a decision was made to establish a Digital Public Infrastructure Repository, and I am pleased to announce its completion. Over 50 DPIs from 16 countries have been incorporated into this repository. To facilitate the implementation of DPIs in Global South nations, I propose the creation of a Social Impact Fund. On India's behalf, I also announce an initial contribution of 25 million dollars to this fund and hope for your participation in this initiative.
        In the era of Artificial Intelligence, there is a need to use technology in a responsible manner. There is growing concern about the negative use of A.I all over the world.
        India firmly believes that we should work together on global regulation of A.I.
        We have to move forward, understanding the seriousness of how dangerous DeepFake is, for society, for the individual.
        We desire that A.I. should reach the people, and it must be safe for the society.
        With this approach, the Global A.I. Partnership Summit is being hosted in India next month.
        And I believe all of you will cooperate in this as well.
        Friends,
        At the New Delhi Summit, I had talked about green credit regarding environmental protection.
        You know that in India we have started it. Through the Global Biofuels Alliance launched in New Delhi, we are reducing carbon as well as promoting the development of alternative fuels.
        The G-20 has recognized mission LiFE, i.e. Lifestyle for Environment, for a pro-planet approach; called for taking renewable energy three times by 2030; shown commitment towards clean hydrogen; recognized the need to take climate finance from billions to trillions.
        In a few days, during the COP-28 which will be held in the UAE, concrete steps need to be taken on all these initiatives.
        Friends,
        A new working group on women empowerment has also been formed.
        In this context, I am very happy to share that India has taken a historic decision in the first session of its new Parliament House.
        To strengthen women-led development, we have decided for 33% reservation for women in Parliament and state legislative assemblies.
        """
    li=str2.split()
    d={}
    for i in li:
        if i not in d.keys():
            d[i]=0
        d[i]=d[i]+1
    print(d)

frequencies=freq_words()
#print(*frequency.items(), sep='\n')
#frequency
#p=dir(dict)
#print(p)
#print(frequencies.keys())
type(frequencies)