# this is the file for setting up the #information
# channel in the Discord server

import discord

dark_blue = 0x6b8095  # (for headings)
light_blue = 0x9ab8d6  # (for text)

# heading_1
heading_1 = discord.Embed(
    color=dark_blue
).set_image(
    url="https://cdn.discordapp.com/attachments/734101751099293788/"
        "734800608443498576/ascendancywavetest-01.png"
)

# text_1
text_1 = discord.Embed(
    description="Whether you’re from the communities of Minecraft "
                "Civilization-genre servers of the past or present, familiar "
                "with the previous community we were affiliated with, or just "
                "stumbling across our side of the Internet, thank you for "
                "joining "
                "us! With Ascendancy: A Minecraft Civilization Project, our "
                "ultimate goal is to host a feedback-driven and feature-full "
                "sociopolitical Minecraft server with custom topography that "
                "revolves around geopolitics and promotes a sense of "
                "wonder and "
                "adventure. *We thank you for your interest and "
                "look forward to "
                "building the next generation of Minecraft Civilization-genre "
                "servers with you!*\n\n"
                "We invite you to [check out our website]"
                "(https://www.ascendancyproject.com/) and "
                "[subreddit community]"
                "(https://www.reddit.com/r/mc_ascendancy/)!",
    color=light_blue
).set_author(
    name="Welcome to the official Discord for Ascendancy: A Minecraft "
         "Civilization Project!"
)

# heading_2
heading_2 = discord.Embed(
    color=dark_blue
).set_image(
    url="https://cdn.discordapp.com/attachments/734102206860623883/"
        "734810657404485662/ACHANNELS-01.png"
)

# text_2
text_2 = discord.Embed(
    description="<#734098917867782214>: Where all these embeds are posted and will "
                "be updated if applicable.\n"
                "<#734098962570805328>: Important updates for our community.",
    color=light_blue
).set_author(
    name="Meta Channels"
)

# text_3
text_3 = discord.Embed(
    description="<#734122828613288059>: A Hall of Fame for your genius "
                "feature "
                "requests and ridiculous memes. Messages need six :star: "
                "reactions "
                "to be archived in this channel.\n"
                "<#734098616460902470>: The place for general discussion. "
                "Need we say more?\n"
                "<#734098725932367944>: Somewhere to share your very funny "
                "memes. Ha. <:wheeze:734034980857970779>\n"
                "<#734098868978843710>: The most important General Channel "
                "of all. If you have any feedback "
                "regarding the Discord server, "
                "subreddit, or (eventually) Minecraft server, post it here! "
                "We will be sure to follow up with and apply your relevant "
                "recommendations.\n"
                "<#735215466968121386>: A place for more niche conversations. "
                "Remember that all server rules still apply in this channel.\n"
                "<#734098831007940648>: A channel for using bots, you alts.\n"
                "<#734119161437093889>: An archive of posts from "
                "[our subreddit community]"
                "(https://www.reddit.com/r/mc_ascendancy/).",
    color=light_blue
).set_author(
    name="General Channels"
)

# text_4
text_4 = discord.Embed(
    description="<#734099995392868352>: A channel for those who prefer"
                " to text chat.\n"
                "General: A voice channel for general discussion.\n"
                "Specific: A voice channel for user-made bots.\n"
                "Music: Raise the roof.\n"
                "AFK: Where the alts go.",
    color=light_blue
).set_author(
    name="Voice Channels"
)

# heading_3
heading_3 = discord.Embed(
    color=dark_blue
).set_image(
    url="https://cdn.discordapp.com/attachments/734102206860623883/"
        "734810659723804682/AROLES-01.png"
)

# text_5
text_5 = discord.Embed(
    description="The leadership hierarchy of this Discord, as well as the "
                "subreddit and Minecraft server, is very simple: *it doesn't "
                "exist*. The only leadership role within our community is "
                "<@&734100717874446396> "
                "and all of our Staff members hold this role "
                "with equal weight. "
                "Each member of our Staff has specialized "
                "into one of three content "
                "roles to further the development of Ascendancy. "
                "These roles are "
                "<@&734212470024962128>, <@&734212404618985543>, and "
                "<@&734212189526818946>.\n\n"
                "Developing in these content-driven roles is "
                "the priority of our "
                "Staff, but some Staff members have also volunteered to be "
                "<@&734097025574109274> and <@&734881814023372801>. "
                "This is not an additional title. Instead, "
                "these Staff members are just ensuring "
                "our front door remains clean.\n\n"
                "[Click here to see who’s who on the Staff team.]"
                "(https://www.ascendancyproject.com/about)",
    color=light_blue
).set_author(
    name="Staff Roles"
)

# text_6
text_6 = discord.Embed(
    description="Those with the <@&734418804490240061> role are "
                "extremely generous "
                "members of our community "
                "who have been so kind as to give the "
                "Discord server additional "
                "perks. These fantastic people are the "
                "reason we’re able to have "
                "as many custom emotes as you’d like!",
    color=light_blue
).set_author(
    name="Server Booster"
)

# text_7
text_7 = discord.Embed(
    description="Those with the <@&734096990396350515> role are the backbone "
                "of our community… indeed, "
                "they are *the* community. They are the "
                "reason we continue "
                "to be dedicated to this project and to "
                "them, we owe our most "
                "sincere thanks.",
    color=light_blue
).set_author(
    name="Member"
)

# heading_4
heading_4 = discord.Embed(
    color=dark_blue
).set_image(
    url="https://cdn.discordapp.com/attachments/734102206860623883/"
        "734810661535612998/ARULES-01.png"
)

# text_8
text_8 = discord.Embed(
    description="We want Ascendancy to develop in a "
                "productive and positive way. "
                "A zero-tolerance policy exists for "
                "any content submitted on "
                "the Discord that is understood to be racist, sexist, ageist, "
                "homophobic, transphobic, ableist, or "
                "generally hate-promoting.",
    color=light_blue
).set_author(
    name="1. No harassment or personal attacks."
)

# text_9
text_9 = discord.Embed(
    description="Don't like a prospective feature? Having doubts about the "
                "development of the server? Growing "
                "frustrated with the timeline? "
                "Have an issue with a Staff member? These are all perfectly "
                "reasonable concerns to have. Ultimately, Ascendancy is a "
                "passion project and one we are "
                "developing so you, the player, "
                "can enjoy it. If you have "
                "criticism, please don't hold back... "
                "but, also make it constructive so that we may apply "
                "it in useful ways!",
    color=light_blue
).set_author(
    name="2. Be honest... but constructive."
)

# text_10
text_10 = discord.Embed(
    description="Don't be obnoxious. You know exactly "
                "what we mean by this rule, "
                "and if you are unsure if a message "
                "is potentially rule-breaking, "
                "send any of our Discord Staff a DM first.",
    color=light_blue
).set_author(
    name="3. Remember the human and use common sense."
)

# text_11
text_11 = discord.Embed(
    description="You want to dominate? Sure, go "
                "ahead: the consequences of being "
                "a vicious ruler are sure to come "
                "eventually. After all, you "
                "write your own story on Ascendancy. However, a line must be "
                "drawn between justifiable destruction "
                "and domination and generally "
                "making the Minecraft server (or Discord) "
                "unpleasant for everyone "
                "else involved. Don't be *that* guy. "
                "You know *that* guy... don't be him.",
    color=light_blue
).set_author(
    name="4. No king of the ashes."
)

# text_12
text_12 = discord.Embed(
    description="Don't promote yourself and your "
                "services or other products and "
                "their respective services on this "
                "Discord server. It's annoying, "
                "unnecessary, and there are certainly "
                "many, many avenues for "
                "advertisement. For better or for "
                "worse, here is not one of them.",
    color=light_blue
).set_author(
    name="5. No promotion of any kind."
)

# text_13
text_13 = discord.Embed(
    description="Don't be rude. Don't spam. If you are "
                "uncertain where a message "
                "might fall in regard to \"No spamming,\" contact one of our "
                "Discord Staff! They will respond as soon as they can, and it "
                "saves all of us avoidable headaches.",
    color=light_blue
).set_author(
    name="6. No spamming."
)

# a collection of all the embeds in order
collection = (
    heading_1,
    text_1,
    heading_2,
    text_2,
    text_3,
    text_4,
    heading_3,
    text_5,
    text_6,
    text_7,
    heading_4,
    text_8,
    text_9,
    text_10,
    text_11,
    text_12,
    text_13
)
