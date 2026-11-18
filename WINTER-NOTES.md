# Winter & Holiday Guide: hand-off notes

`winter.html` is the winter version of the summer list (`index.html`). Same look, filters and EN/ES toggle.
Edit listings in `tools/winter_data.py`, then run:

    python3 tools/build_winter.py

The build checks every card (fields, counties, types, dates, https links, Spanish text) before it writes `winter.html`.

What's new compared to summer:
- **Holiday Help** filter and a callout box that jumps straight to it.
- **Sign-up deadlines** (`deadline:`). Open sign-ups sort to the top, soonest first. After the date, the card greys out and says "Sign-up closed."
- **Self-expiring events** (`until:`). A one-day event hides itself the day after it happens, so the page reads right whenever it's posted.
- Link straight to a view: `winter.html?type=help`, `winter.html?lang=es`, or both.
- Filters stay pinned while scrolling on desktop, but not on phones (they covered half the screen).

## Squarespace page

The summer page and `index.html` stay as they are. The summer page is deactivated in Squarespace, not deleted.

1. Make a new page with the URL slug `/winter`.
2. Add a Code block with this embed (same settings as the summer one):

```html
<iframe
  src="https://kate-rose.github.io/gorge-kids-activities/winter.html"
  width="100%"
  height="900"
  style="border: none; border-radius: 12px; display: block;"
  title="Free Winter & Holiday Help for Gorge Families 2026–27"
  loading="lazy">
</iframe>
```
3. Page text:

**Heading:** The Open Gorge Winter Survival Guide:
**Subheading:** Free Holiday Help & Low-Cost Kids Activities

**Intro:** Winter break, holiday gifts, a turkey on the table, the heating bill. It all lands at once. Families shouldn't have to spend hours hunting for help or for things to do with the kids. This is a living list of free holiday help and free or under-$10 winter activities across Skamania, Klickitat, Hood River and Wasco counties. Many gift and meal sign-ups close in early December, so start with the Holiday Help button.

**Help Us Keep This Growing!** Know a toy drive, a free holiday dinner, a coat giveaway, or a free winter-break activity we missed? Send it our way.

## Check before posting

- **Hood River County Christmas Project:** registration closes **Sat, Nov 21, 2026**. Worth a share in the newsletter or on social right away.
- **Skamania Christmas Basket:** the form says "Thursday, December 4 at 5:30 PM," but Dec 4, 2026 is a Friday. The card tells families to send it in by **Thu, Dec 3** to be safe. One email to parks@skamaniacounty.gov would settle it.
- **Goldendale Giving Tree:** the only phone number (Taletha Wagoner, 509-493-3716) appeared in a donor context in Columbia Gorge News. Confirm it's also the right number for families.
- **MCCAC heating help:** the page says both "no energy assistance available at this time" and "appointments start Dec 1," with no year on either. The card tells families to call and ask.
- **Little John Sno-Park is closed** (Grasshopper Fire order, through Dec 31, 2027). The sledding card points to White River West instead.

## Left out on purpose (no 2026 confirmation yet; add if they post)

| Program | Why it's held |
|---|---|
| Goldendale Candy Cane Lane Parade | Latest dates found are from 2024 and 2025 |
| Goldendale Holiday Family Craft Night | 2025 date only |
| Dufur Hometown Christmas | 2026 date not posted |
| The Dalles Community Thanksgiving (Salvation Army) | Last confirmed Nov 2024; not on CGN's Nov 2026 calendar |
| FISH holiday distribution, Cascade Locks | "Wednesday, December 15" doesn't match 2026 (Dec 15 is a Tuesday) |
| Hood River Adventist food bank & clothing day | Address and hours conflict between sources |
| Cooper Spur (kids 6 & under ski free) | 2026–27 season not posted |
| Teacup Nordic (kids ski free) | Adults pay $25, so a family trip is over $10 |
| CASS Art Hives | No winter dates posted |
| Oregon State Parks First Day Hikes | No Gorge park on the list yet; free parking ended |

Nobody found a Toys for Tots campaign covering any of the four counties.
