/**
 * A repository label, coloured the way GitHub colours it.
 *
 * The chip carries the label's own hex rather than a palette of ours: a
 * maintainer recognises their `good first issue` green before they read it, and
 * a recoloured chip costs that. The arithmetic that turns one hex into a
 * readable foreground, background and border is Primer's, in `.chip` -- all
 * this does is hand it the channels it wants.
 */
export function Label({ name, hex }: { name: string; hex: string | undefined }) {
  const channels = hex ? decompose(hex) : undefined;

  if (!channels) {
    return (
      <span className="h-[18px] shrink-0 rounded-full border border-border px-1.5 text-[10px] leading-4 text-muted-foreground">
        {name}
      </span>
    );
  }

  return (
    <span
      className="chip h-[18px] shrink-0 rounded-full border px-1.5 text-[10px] leading-4 font-medium"
      style={
        {
          "--label-r": channels.r,
          "--label-g": channels.g,
          "--label-b": channels.b,
          "--label-h": channels.h,
          "--label-s": channels.s,
          "--label-l": channels.l,
        } as React.CSSProperties
      }
    >
      {name}
    </span>
  );
}

interface Channels {
  r: number;
  g: number;
  b: number;
  h: number;
  s: number;
  l: number;
}

/** Split `d73a4a` into the six numbers Primer's formulas are written against. */
function decompose(hex: string): Channels | undefined {
  const digits = hex.replace(/^#/, "");
  if (!/^[0-9a-f]{6}$/i.test(digits)) return undefined;

  const r = parseInt(digits.slice(0, 2), 16);
  const g = parseInt(digits.slice(2, 4), 16);
  const b = parseInt(digits.slice(4, 6), 16);

  const [red, green, blue] = [r / 255, g / 255, b / 255];
  const high = Math.max(red, green, blue);
  const low = Math.min(red, green, blue);
  const spread = high - low;
  const l = (high + low) / 2;

  let h = 0;
  if (spread !== 0) {
    if (high === red) h = ((green - blue) / spread) % 6;
    else if (high === green) h = (blue - red) / spread + 2;
    else h = (red - green) / spread + 4;
    h *= 60;
    if (h < 0) h += 360;
  }
  const s = spread === 0 ? 0 : spread / (1 - Math.abs(2 * l - 1));

  return {
    r,
    g,
    b,
    h: Math.round(h),
    s: Math.round(s * 100),
    l: Math.round(l * 100),
  };
}
