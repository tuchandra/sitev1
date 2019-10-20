<!-- imagedir: silph_images -->
<!-- date: 2019-10-17 -->
# Statistical nuance & the importance of uncertainty
In [my last post](silph.md), I re-analyzed shiny rates from The Silph Road and came to the conclusion that their proposed shiny rates were inconsistent with their own data. This post explores how that happened and what we can do to avoid it in the future.

## An ongoing assumption


Silph has, perhaps unknowingly, treated the assumed standard shiny rate of 1 in 450 as fact on several occasions:
 * ["using the base shiny rate of 1 in 450, as expected"](https://thesilphroad.com/science/quick-discovery/ultra-bonus-week-3-shiny-rates/) during the Patrat and Lillipup event
 * ["using the standard 1 in 450 rate"](https://thesilphroad.com/science/quick-discovery/johto-journey-sentret-gligar-shiny-rates/) during the Sentret and Gligar event
 * ["both species are using the standard 1 in 450 shiny rate"](https://thesilphroad.com/science/quick-discovery/water-festival-2019-barboach-and-carvanha-shiny-rates/)) during the Water Festival event

Silph reported 99% confidence intervals alongside their predictions; click any of those links and you'll see it. But these confidence intervals are frequently lost to the audience.

Not Silph: https://old.reddit.com/r/TheSilphRoad/comments/czphox/gligar_shiny_boost/ says from 1 in 450 to 1 in 150.

Saying "the 1 in 450 shiny rate" https://old.reddit.com/r/TheSilphRoad/comments/dd6ln1/world_wide_oddish_shiny_rates/f2emvtr/

Is Silph to blame? Doubtful. I think the only way they could do better is if they chose to report ranges instead of point estimates.

Aggregate all the data and 1 in 150 is squarely outside the confidence interval: https://old.reddit.com/r/TheSilphRoad/comments/dd6ln1/world_wide_oddish_shiny_rates/f2egcsx/

Reddit post on Ekans and Koffing - https://old.reddit.com/r/TheSilphRoad/comments/cigzzu/tsr_team_go_rocket_event_shiny_rates_so_far/ - didn't even report the CIs


https://thesilphroad.com/science/shiny-egg-hatches-field-research-encounter-rates/
> Evidence for some bias in our reporting can be seen when we compare the shiny rates for our newest researchers (who make up a slight majority of our data), and our more seasoned, senior members. Our junior researchers have a shiny rate of 1 in 425, while our more experienced seniors have a shiny rate of 1 in 475. As you might expect, if the probability was actually lower than our reported value, the seniors are closer to the true rate than our junior members. We could therefore speculate that the actual integer value being used is 1 in 500 for the base Wild Encounter shiny rate.

They showed lots of caution here, but the level of uncertainty that they reported decreased with time.


Time to rethink 1 in 450: https://old.reddit.com/r/TheSilphRoad/comments/dd79zk/its_time_to_rethink_the_assumed_shiny_rates_from/



Finally, to Silph's credit: they are a volunteer group of researchers, and few others are doing *any* research into Pokemon GO shiny rates. As the head of Silph [said](https://old.reddit.com/r/TheSilphRoad/comments/dd79zk/its_time_to_rethink_the_assumed_shiny_rates_from/f2esyq8/), the focus of these studies was *not* re-affirming the assumed rate, but rather determining if a particular event had the standard or boosted rate, whatever those are. Their treatment of statistics is far better than the average layperson, and I commend them for that. But I think we can do better.
