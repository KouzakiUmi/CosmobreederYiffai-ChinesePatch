package PRG;

/** Render-only compatibility encoding for the ORIGINAL Pixel Dingbats-7 font.
 * Does not translate, store a second source, mutate amn, or add any glyph/texture.
 * This is a lossy fictional-script representation, NOT encryption/security.
 * One engine UTF-16 reveal cell remains one symbol cell (8px original advance).
 */
public final class PatternSymbols {
    public static final String DINGBATS_SHA256 = "2d2aeba3f9b513ea520958e4271601e9a19ffcbb5663c4596abc45dacd590c19";
    private static final String ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    private PatternSymbols() { }

    /** Only call AFTER the original unreadable-language decision. Operates on
     * the CURRENT mask, never the full caption: hidden spaces cannot leak ink.
     * Legacy exact dingbats characters retain their original symbol identity.
     * Other whitespace becomes the original blank cell; unsupported nonblank
     * units deterministically choose an existing visible symbol, including CJK
     * punctuation. No markup delimiters can be introduced by this mapping.
     * The existing engine is UTF-16 based; supplementary characters deliberately
     * retain its two-cell/two-reveal-step behavior rather than shifting indices.
     * No cache or resource owner/lifecycle is introduced.
     */
    public static String encodeMask(String maskedLine) {
        if (maskedLine == null) throw new NullPointerException("pattern mask");
        char[] changed = null;
        for (int i = 0; i < maskedLine.length(); i++) {
            char source = maskedLine.charAt(i), symbol;
            if (source == ' ' || source == '\n' || source == '\r' || source == '\t'
                    || (source >= 33 && source <= 126) || (source >= 160 && source <= 255)) symbol = source;
            else if (Character.isWhitespace(source) || Character.isSpaceChar(source)) symbol = ' ';
            else symbol = ALPHABET.charAt((source ^ (source >>> 8)) % ALPHABET.length());
            if (symbol != source) {
                if (changed == null) changed = maskedLine.toCharArray();
                changed[i] = symbol;
            }
        }
        return changed == null ? maskedLine : new String(changed);
    }
}
