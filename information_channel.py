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
                "(https://ascendancy.wuzado.com/) and "
                "[subreddit community]"
                "(https://www.reddit.com/r/ascendancy/)!\n\n"
                "Join us at `civ.ascendancyproject.com` (1.16.4).",
    color=light_blue,
    title="Welcome to the official Discord for Ascendancy: A Minecraft "
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
    description="<#734098917867782214>: A channel dedicated to information "
                "about Ascendancy: A Minecraft Civilization Project.\n"
                "<#779218188520652820>: A channel dedicated to players "
                "opting into specific, category-based roles.\n"
                "<#734098962570805328>: A channel for important updates.",
    color=light_blue,
    title="Meta Channels"
)

# text_3
text_3 = discord.Embed(
    description="<#734122828613288059>: A Hall of Fame for your genius "
                "feature requests and ridiculous memes. Messages need six "
                ":star: reactions to be archived in this channel.\n"
                "<#734098616460902470>: The place for general discussion. "
                "Need we say more?\n"
                "<#734098725932367944>: A channel to share your very funny "
                "memes. Ha. <:wheeze:734034980857970779>\n"
                "<#735215466968121386>: A channel for more niche "
                "conversations. Remember that all server rules still apply in "
                "this channel.\n"
                "<#734098831007940648>: A channel for using bots.\n"
                "<#734119161437093889>: An archive of posts from "
                "[our subreddit community]"
                "(https://www.reddit.com/r/ascendancy/).",
    color=light_blue,
    title="General Channels"
)

# text_3a
text_3_ = discord.Embed(
    description="<#788327472365436958>: A channel to get updates about "
                "changes in the Minecraft server.\n"
                "<#788327510810034186>: A place to discuss in-game trading. "
                "(Do keep rule 6e in mind.)\n"
                "<#788327572555431956>: Enjoy this small selection of "
                "screenshots from just a few of our biomes in-game!\n"
                "<#799773411324330054>: You can report bugs here!\n"
                "<#788327594344448021>: The place to report players. "
                "You can also report players in-game by using /report.\n"
                "<#788341976575115264>: The place where you can stay "
                "up-to-date on server events, through our very own "
                "<@733399011230220300>!",
    color=light_blue,
    title="Ascendancy Channels"
)

# text_4
text_4 = discord.Embed(
    description="<#736210100724826124>: A channel dedicated to players "
                "opening tickets related to General Topics, Staff Reports, or "
                "Emote Requests.\n"
                "<#736325021856694385>: A channel for players to suggest "
                "prospective features for the Discord server, subreddit, "
                "Minecraft server, or website.\n"
                "<#736325045617557584>: A channel for players to discuss the "
                "ideas suggested in <#736325021856694385>.\n"
                "<#799669552329785374>: A channel specifically for asking "
                "questions!\n"
                "<#734098868978843710>: A channel for players to give "
                "feedback regarding the Discord server, subreddit, Minecraft "
                "server, or website.",
    color=light_blue,
    title="Development Channels"
)

# text_5
text_5 = discord.Embed(
    description="<#734099995392868352>: A channel for those who prefer"
                " to text chat.\n"
                "General: A voice channel for general discussion.\n"
                "Specific: A voice channel for using user-made bots.\n"
                "Music: Raise the roof.\n"
                "AFK: Exit stage left, please.",
    color=light_blue,
    title="Voice Channels"
)

# heading_3
heading_3 = discord.Embed(
    color=dark_blue
).set_image(
    url="https://cdn.discordapp.com/attachments/734102206860623883/"
        "734810659723804682/AROLES-01.png"
)

# text_6
text_6 = discord.Embed(
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
    color=light_blue,
    title="Staff Roles"
)

# text_7
text_7 = discord.Embed(
    description="Those with the <@&734418804490240061> role are "
                "extremely generous "
                "members of our community "
                "who have been so kind as to give the "
                "Discord server additional "
                "perks. These fantastic people are the "
                "reason we’re able to have "
                "as many custom emotes as you’d like!",
    color=light_blue,
    title="Server Booster"
)

# text_8
text_8 = discord.Embed(
    description="Those with the <@&734096990396350515> role are the backbone "
                "of our community… indeed, "
                "they are *the* community. They are the "
                "reason we continue "
                "to be dedicated to this project and to "
                "them, we owe our most "
                "sincere thanks.",
    color=light_blue,
    title="Member"
)

# heading_4
heading_4 = discord.Embed(
    color=dark_blue
).set_image(
    url="https://cdn.discordapp.com/attachments/734102206860623883/734810661535612998/ARULES-01.png"
)

# heading_4_
heading_4_ = discord.Embed(
    description="*All rules and policies are up to the interpretation of the "
                "Staff. Just be kind and you'll never have to worry about "
                "these.*",
    color=light_blue
)

# text_9
text_9 = discord.Embed(
    description="**a.** We want Ascendancy to develop in a productive and "
                "positive way. A zero-tolerance policy exists for any content "
                "submitted on the Discord server, subreddit, or Minecraft "
                "server that is understood to be racist, sexist, ageist, "
                "homophobic, transphobic, ableist, or generally "
                "hate-promoting.\n\n"
                "**b.** You may not share the personal information of another "
                "player under any circumstances without their explicit "
                "consent. You may repeat information that a player has "
                "publicly shared about themselves.\n\n"
                "**c.** Due to the competitive nature of the Minecraft "
                "server, we expect there to be conflict and disagreements "
                "between players. We also expect that you always remain civil "
                "in your interactions with others.",
    color=light_blue,
    title="1. No harassment or personal attacks."
)

# text_10
text_10 = discord.Embed(
    description="**a.** Don't like a prospective feature? Having doubts about "
                "the development of the server? Growing frustrated with the "
                "timeline? Have an issue with a Staff member? These are all "
                "perfectly reasonable concerns to have. Ultimately, "
                "Ascendancy is a passion project and one we are developing so "
                "you, the player, can enjoy it. If you have criticism, please "
                "don't hold back... but make it constructive so that we may "
                "apply it in useful ways!\n\n"
                "**b.** Every Staff member of Ascendancy is currently an "
                "unpaid volunteer. We'd rather spend our time developing than "
                "sorting out obnoxious and petty issues on the Discord "
                "server, subreddit, or Minecraft server. Please use common "
                "sense, and if you are unsure if a message or action is "
                "potentially rule-violating, submit a General Topics ticket "
                "in the #tickets channel of our Discord or utilize [the "
                "modmail feature]"
                "(https://reddit.com/message/compose?to=/r/ascendancy).\n\n"
                "**c.** Do not exploit bugs. All bugs and exploits recognized "
                "must be reported to the Staff as soon as practicable. Any "
                "distribution or public posting about replicating a bug or "
                "exploit is not allowed.",
    color=light_blue,
    title="2. Be honest... but constructive. Do not exploit bugs."
)

# text_11
text_11 = discord.Embed(
    description="**a.** You want to dominate? Sure, go ahead: the "
                "consequences of being a vicious ruler are sure to come "
                "eventually. After all, you write your own story on "
                "Ascendancy. However, a line must be drawn between "
                "justifiable destruction and domination and generally making "
                "the Discord server, subreddit, or Minecraft server "
                "unpleasant for everyone else involved. In short, you don’t "
                "need to be friends with everyone… but be friendly.",
    color=light_blue,
    title="3. No king of the ashes."
)

# text_12
text_12 = discord.Embed(
    description="**a.** Don't promote yourself and your services or other "
                "products and their respective services on the Discord "
                "server, subreddit, or Minecraft server. It's annoying, "
                "unnecessary, and there are certainly many, many avenues for "
                "advertisement. For better or for worse, here is not one of "
                "them.\n\n"
                "**b.** If you want permission to advertise other services, "
                "you must first submit a General Topics ticket in the "
                "<#736210100724826124> channel of our Discord or utilize [the "
                "modmail feature]"
                "(https://reddit.com/message/compose?to=/r/ascendancy) "
                "to receive explicit permission.",
    color=light_blue,
    title="4. No promotion of any kind."
)

# text_13
text_13 = discord.Embed(
    description="**a.** Don't be rude. Don't spam. We have specific channels "
                "on the Discord server and specific post flairs on the "
                "subreddit: use them for their intended purposes.\n\n"
                "**b.** If you are unsure if a certain topic might violate "
                "this rule, you must submit a General Topics ticket in the "
                "<#736210100724826124> channel of our Discord, request a "
                "specific channel or post flair to be added in the "
                "<#734098868978843710> channel of our Discord, or utilize "
                "[the modmail feature]"
                "(https://reddit.com/message/compose?to=/r/ascendancy).\n\n"
                "**c.** Regardless of intent, you may not share sexually "
                "implicit or explicit content of any kind on any of our "
                "services.\n\n"
                "**d.** Regardless of intent, any media with a suggestive "
                "quality depicting an individual who could reasonably be "
                "interpreted as a minor is not allowed on any of our services.",
    color=light_blue,
    title="5. No spamming. No NSFW content."
)

# text_14
text_14 = discord.Embed(
    description="**a.** Alternate accounts of any kind are not allowed on the "
                "Discord server, subreddit, or Minecraft server. If you are "
                "found to be using an alternate account, you will be banned "
                "from all our services on all accounts. Using an alternate "
                "account to circumvent any punishment is also against our "
                "rules.\n\n"
                "**b.** Regardless of intent, you may not assist or encourage "
                "another player to violate any of our rules.\n\n"
                "**c.** You may not trade in-game goods or services for "
                "out-of-game goods or services, or vice versa.",
    color=light_blue,
    title="6. Miscellaneous rules."
)

# heading_m
heading_m = discord.Embed(
    color=dark_blue
).set_image(
    url="https://cdn.discordapp.com/attachments/734117420888883231/802007197818814494/MCRULES-01.png"
)

# heading_m_
heading_m_ = discord.Embed(
    description="*These rules serve as additions— not substitutions— for all "
                "the rules listed above and all the policies listed below "
                "when connected to our Minecraft server.*",
    color=light_blue
)

# text_m7
text_m7 = discord.Embed(
    description="**a.** Everything that your player does in-game must be done "
                "by you and your human inputs. Violations of this rule "
                "include but are not limited to: bypassing AFK checks; AFK "
                "fishing; macros of any kind.\n\n"
                "**b.** You may not use illegal client-side mods, bugs, or "
                "unintended game mechanics to gain an unfair competitive "
                "advantage. Violations of this rule include but are not "
                "limited to: duping; x-raying; flying; bug exploitation; "
                "glitch exploitation; intentionally causing lag, server or "
                "otherwise; intentionally misusing game mechanics, server or "
                "otherwise.\n\n"
                "**c.** You may not utilize a VPN, VPS, or any form of proxy "
                "to connect to our Minecraft server.",
    color=light_blue,
    title="7. No botting or hacking. No VPN usage."
)

# text_m8
text_m8 = discord.Embed(
    description="**a.** At this time, these are the only approved client-side "
                "mods: OptiFine; VoxelMap; JourneyMap; LambDynamicLights; "
                "LogicalZoom.\n\n"
                "**b.** You may not utilize any client modification that "
                "allows you to create an offline version of our Minecraft "
                "server’s map.\n\n"
                "**c.** If you would like to use other client-side mods, you "
                "must first submit a General Topics ticket in the "
                "<#736210100724826124> channel of our Discord or utilize the "
                "modmail feature to receive explicit permission. Through your "
                "recommendations, we can expand this list and further approve "
                "and support other client-side mods. Do not assume we’ll "
                "allow what you intend to use— ask first.",
    color=light_blue,
    title="8. No use of unapproved client-side mods."
)

# text_15
text_15 = discord.Embed(
    description="The Staff of Ascendancy: A Minecraft Civilization Project "
                "reserve the right to remove any player for any reason for "
                "any length of time from the Discord server, subreddit, or "
                "Minecraft server. Our rules and policies are up to the "
                "interpretation of the Staff. Additionally, our rules may "
                "be changed at any time, and, as a player, you will always "
                "be held to them. We will do our best to update the "
                "community on any rule modifications, additions, or "
                "subtractions as soon as possible. We also reserve the right "
                "to punish retroactively with rule changes if at all necessary.\n\n"
                "As a Staff, our deepest motivation is to develop a "
                "feedback-driven and feature-full Minecraft Civilization server. "
                "We need a community to accomplish this goal, and, therefore, "
                "no punishment is ever given lightly. Especially punishments "
                "that warrant us removing a community member entirely. With "
                "that said, the punishment is subject to the crime, and we "
                "expect players to interact with others with a certain level of "
                "mutual respect.\n\n"
                "If you ever have concerns or confusion regarding any of our "
                "rules, submit a General Topics ticket in the <#736210100724826124> "
                "channel or use "
                "[the modmail feature](https://reddit.com/message/compose?to=/r/ascendancy). "
                "Though we understand it may be more convenient to direct message a "
                "Staff member on Discord, your question may not be answered with "
                "satisfaction or accuracy if you only consult with one Staff "
                "member. Consider Discord tickets or modmail as your first point of "
                "contact with the Staff. By using Discord tickets or modmail, "
                "you are likely to get a more accurate and legitimate answer: "
                "we are a group of Staff, and we discuss and make decisions as "
                "a group. An answer you receive from a single Staff member "
                "could be overturned by the majority. If you would like to "
                "appeal punishments, you must do so through the modmail "
                "feature. We will not discuss bans publicly, and if you direct "
                "message a Staff member on Discord or Reddit regarding a "
                "punishment or appeal, it will be ignored.",
    color=light_blue,
    title="Hammer to Fall Policy"
)

# text_16
text_16 = discord.Embed(
    description="Any reports against either members of the community or "
                "Staff, must be submitted utilizing our ticket system, "
                "directly reporting the user to Discord, or directly "
                "reporting the user to Reddit. Any other means of "
                "confronting members or Staff for rule violations, on any of "
                "our services or through private message, is not permitted "
                "and will be treated as harassment.",
    color=light_blue,
    title="Reporting Policy"
)

# text_17
text_17 = discord.Embed(
    description="If a user's commentary or actions on one of our services may "
                "cause a liability— harassment or otherwise— on any of our "
                "other services, we reserve the right to remove this player "
                "from participating on all other services, regardless of "
                "which service the initial commentary or action originated."
                "\n\n"
                "This Social Rules Policy is governed by Rule 1, subsections "
                "a., b., and c., Rule 3, subsection a., Rule 4, subsection "
                "a., Rule 5, subsection a., c., d., and Rule 6, subsection "
                "b. This list may expand. By “our services,” we mean our "
                "Discord server, our subreddit, our Minecraft servers, and "
                "our public GitHub pages. This list may expand.",
    color=light_blue,
    title="Social Rules Policy"
)

# text_18
text_18 = discord.Embed(
    color=light_blue,
    title="Minecraft Server"
).add_field(
    name="Address",
    value="`civ.ascendancyproject.com`",
    inline=True
).add_field(
    name="Version",
    value="1.16.4",
    inline=True
)

# a collection of all the embeds in order
collection = (
    heading_1,
    text_1,
    heading_2,
    text_2,
    text_3,
    text_3_,
    text_4,
    text_5,
    heading_3,
    text_6,
    text_7,
    text_8,
    heading_4,
    heading_4_,
    text_9,
    text_10,
    text_11,
    text_12,
    text_13,
    text_14,
    heading_m,
    heading_m_,
    text_m7,
    text_m8,
    text_15,
    text_16,
    text_17,
    text_18
)
