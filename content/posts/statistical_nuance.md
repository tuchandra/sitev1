<!-- date: 2019-10-17 -->
# Statistical nuance & the importance of uncertainty
In [my last post](silph.md), I re-analyzed shiny rates from The Silph Road and came to the conclusion that their proposed shiny rates were inconsistent with their own data. This post explores how that happened and what we can do to avoid it in the future.

## On the knowability of the shiny rates
People often talk about the various shiny rates as though they are known as truth. This, obviously, is not correct; unless Niantic publishes the various shiny rates somewhere, we can never be completely certain of them (*). Thinking about them as fact can also lead us astray, as my [previous post](silph.md) demonstrated. The best that we can do is to collect data in support of particular hypotheses, which is often very good.

Collecting this data lets us come close to truth--close enough that this discussion can sometimes be dismissed as pedantic. There is overwhelming evidence to suggest that Community Day events have a shiny rate of 1 in 25, regular legendary raids 1 in 20, and Raid Day events 1 in 10, and I have no reason to doubt that.

This is useful. If we take the raid day shiny rate of 1 in 10 to be true, we can say things like "after 10 raids, you have a 66% chance of getting a shiny. To have a 95% chance, you have to do 28 raids." This is easy to understand and enables players to plan for these events. In other words: it's true to say that we can never *know* the true shiny rate. But saying that misses the point when the evidence suggests that we're very close.

(*) Note, also, that recent attempts at legislating loot boxes [may force this](https://old.reddit.com/r/TheSilphRoad/comments/c2i7hc/would_pokemon_go_be_affected_by_recently_proposed/). I'll leave the interpretation of these bills to someone with more legal expertise than me.

## On probability
The previous discussion is one of terminology, but there's also something to be said about probability here. Posts like [this one](https://old.reddit.com/r/TheSilphRoad/comments/a08bqg/psa_shiny_rates_in_pogo/) explain why someone can do 10 raids, each with a shiny rate of 1 in 10, without seeing a shiny. The concept is no different from drawing without replacement, but it's one thing to write this here and another for everyone to reason logically about it. Add in the emotions of feeling unlucky, or the money spent purchasing premium items to improve your odds, and it's hard not to feel like you're "owed" a shiny after some time.

This leads to people wondering if shiny rates have been lowered: [here](https://old.reddit.com/r/TheSilphRoad/comments/aub8un/lower_shiny_rate_for_latias/) [are](https://old.reddit.com/r/TheSilphRoad/comments/94jllg/does_roselia_have_a_lower_shiny_rate_than_others/) [four](https://old.reddit.com/r/TheSilphRoad/comments/b4ncoy/treecko_shiny_rate/) [examples](https://old.reddit.com/r/TheSilphRoad/comments/96gjab/i_caught_96_eevees_today_and_not_a_single_one_was/) from searching "lower shiny rate" on /r/TheSilphRoad. The reality, of course, is that we all get unlucky sometimes.

I don't mean this to be "hah, I'm smarter than you all, look how rational I am"--I feel the same way when I've done 10 raid day events or 30 normal legendary raids without a shiny. The reality of this is that reasoning about probabilities is *hard*, and that we all look at the world with some degree of [self-serving bias](https://en.wikipedia.org/wiki/Self-serving_bias), and that it's *very, very difficult* to stop these from getting in the way of objective science.

## On the importance of uncertainty
Silph has, perhaps unknowingly, treated the assumed standard shiny rate of 1 in 450 as fact on several occasions:
 * ["using the base shiny rate of 1 in 450, as expected"](https://thesilphroad.com/science/quick-discovery/ultra-bonus-week-3-shiny-rates/) during the Patrat and Lillipup event
 * ["using the standard 1 in 450 rate"](https://thesilphroad.com/science/quick-discovery/johto-journey-sentret-gligar-shiny-rates/) during the Sentret and Gligar event
 * ["both species are using the standard 1 in 450 shiny rate"](https://thesilphroad.com/science/quick-discovery/water-festival-2019-barboach-and-carvanha-shiny-rates/)) during the Water Festival event

Silph reported 99% confidence intervals alongside their predictions; click any of those links and you'll see it. But these confidence intervals are frequently lost to the audience when there's a nice, big "1 in 450" on the page, and the description of the table treats 1 in 450 as truth.

This leads to others propogating the point estimate. Here are a handful of examples: [1](https://old.reddit.com/r/TheSilphRoad/comments/czphox/gligar_shiny_boost/), [2](https://old.reddit.com/r/TheSilphRoad/comments/dd6ln1/world_wide_oddish_shiny_rates/f2emvtr/), [3](https://old.reddit.com/r/TheSilphRoad/comments/cigzzu/tsr_team_go_rocket_event_shiny_rates_so_far/). The last example went so far as to reproduce one of Silph research posts without including the confidence intervals.

Eventually, someone [brought this up](https://old.reddit.com/r/TheSilphRoad/comments/dd79zk/its_time_to_rethink_the_assumed_shiny_rates_from/) on the Silph subreddit, but they attributed the shiny rates to the Silph research group. I don't know that this is fair to Silph; while it's true they proposed the shiny rates originally, the subreddit members had just as much of a role in spreading the assumed rates as the research group. The treatment of uncertainty was simply lost over time.

## On Silph
Back in 2018, Silph posted a three-part study about *all* the shiny rates in the game. [Part III](https://thesilphroad.com/science/shiny-egg-hatches-field-research-encounter-rates/) is the most interesting:

> Evidence for some bias in our reporting can be seen when we compare the shiny rates for our newest researchers (who make up a slight majority of our data), and our more seasoned, senior members. Our junior researchers have a shiny rate of 1 in 425, while our more experienced seniors have a shiny rate of 1 in 475. As you might expect, if the probability was actually lower than our reported value, the seniors are closer to the true rate than our junior members. We could therefore speculate that the actual integer value being used is 1 in 500 for the base Wild Encounter shiny rate.

They showed lots of caution here. A critical part of research is being careful about possible biases and sources of error in your methodology, and Silph did exactly that. Unfortunately, as time went on, they started reporting this kind of uncertainy less and less frequently (see the examples above), and few people remember that they posted this methodological note a year ago.

Finally, to Silph's credit: they are a volunteer group of researchers, and few others are doing *any* research into Pokemon GO shiny rates. As the head of Silph [said](https://old.reddit.com/r/TheSilphRoad/comments/dd79zk/its_time_to_rethink_the_assumed_shiny_rates_from/f2esyq8/), the focus of most of these studies was *not* re-affirming the assumed rate, but rather determining if a particular event had the standard or boosted rate, whatever those may be. Their treatment of statistics is far better than the average layperson, and I appreciate their efforts to increase statistical literacy in the Pokemon GO community.
