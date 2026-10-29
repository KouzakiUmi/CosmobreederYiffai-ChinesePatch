package PRG;

/** Display-only radio labels. Never use these values as dialogue/portrait IDs. */
public final class RadioLabels {
    private RadioLabels() {}

    /** Labels use the original 8px grid, including the six-column frequency field. */
    public static void draw(SN sn, String text, int x, int y, String role) {
        sn.a(text, x, y, localized(text) ? "classic" : role);
    }

    @SuppressWarnings({"rawtypes", "unchecked"})
    public static void drawTint(SN sn, String text, int x, int y, aBa color, String role) {
        sn.a(text, x, y, color, localized(text) ? "classic" : role);
    }

    // Generated from translations/character-names.json; independently reviewed localization names.
    private static boolean localized(String text) {
        return text != null && (text.contains("毛鼠")
            || text.contains("雄猫")
            || text.contains("伊吠")
            || text.contains("伊吠妮")
            || text.contains("波苏")
            || text.contains("麦森")
            || text.contains("季高")
            || text.contains("星杀")
            || text.contains("约戈")
            || text.contains("邦妮琳")
            || text.contains("卡尔")
            || text.contains("彗珂")
            || text.contains("艾玛")
            || text.contains("黛蕾")
            || text.contains("南布")
            || text.contains("维克斯")
            || text.contains("塞塔特尼")
            || text.contains("高鲁")
            || text.contains("猎豹")
            || text.contains("特鲁维洛")
            || text.contains("伏尔甘")
            || text.contains("亨舍尔")
            || text.contains("弗兰基")
            || text.contains("绍狞")
            || text.contains("卡宾")
            || text.contains("潘科")
            || text.contains("红牛")
            || text.contains("恩莉耶")
            || text.contains("猪哥布林")
            || text.contains("狼犬")
            || text.contains("狼崽")
            || text.contains("雅科夫"));
    }

    /** Exact names only: never infer hidden actors or rewrite script keys. */
    public static String display(String name) {
        if ("Mauser".equalsIgnoreCase(name)) return "毛鼠";
        if ("Tomcat".equalsIgnoreCase(name)) return "雄猫";
        if ("Yiffai".equalsIgnoreCase(name)) return "伊吠";
        if ("Yiffany".equalsIgnoreCase(name)) return "伊吠妮";
        if ("Yifany".equalsIgnoreCase(name)) return "伊吠妮";
        if ("Bossu".equalsIgnoreCase(name)) return "波苏";
        if ("Macsen".equalsIgnoreCase(name)) return "麦森";
        if ("The0".equalsIgnoreCase(name)) return name;
        if ("Gitgud".equalsIgnoreCase(name)) return "季高";
        if ("Starkill".equalsIgnoreCase(name)) return "星杀";
        if ("Yogo".equalsIgnoreCase(name)) return "约戈";
        if ("Buntleen".equalsIgnoreCase(name)) return "邦妮琳";
        if ("Kahr".equalsIgnoreCase(name)) return "卡尔";
        if ("Komet".equalsIgnoreCase(name)) return "彗珂";
        if ("Erma".equalsIgnoreCase(name)) return "艾玛";
        if ("Daleir".equalsIgnoreCase(name)) return "黛蕾";
        if ("Nambu".equalsIgnoreCase(name)) return "南布";
        if ("Vickers".equalsIgnoreCase(name)) return "维克斯";
        if ("Cetartni".equalsIgnoreCase(name)) return "塞塔特尼";
        if ("Gaoru".equalsIgnoreCase(name)) return "高鲁";
        if ("Gepard".equalsIgnoreCase(name)) return "猎豹";
        if ("Truvelo".equalsIgnoreCase(name)) return "特鲁维洛";
        if ("Vulcan".equalsIgnoreCase(name)) return "伏尔甘";
        if ("Henschel".equalsIgnoreCase(name)) return "亨舍尔";
        if ("Franchi".equalsIgnoreCase(name)) return "弗兰基";
        if ("Chauchat".equalsIgnoreCase(name)) return "绍狞";
        if ("Karbine".equalsIgnoreCase(name)) return "卡宾";
        if ("Pancor".equalsIgnoreCase(name)) return "潘科";
        if ("Redbull".equalsIgnoreCase(name)) return "红牛";
        if ("Enelye".equalsIgnoreCase(name)) return "恩莉耶";
        if ("Pigobin".equalsIgnoreCase(name)) return "猪哥布林";
        if ("Traeh".equalsIgnoreCase(name)) return "Traeh";
        if ("Werehund".equalsIgnoreCase(name)) return "狼犬";
        if ("Werepup".equalsIgnoreCase(name)) return "狼崽";
        if ("Sevaw".equalsIgnoreCase(name)) return "Sevaw";
        if ("Erauqs".equalsIgnoreCase(name)) return "Erauqs";
        if ("Jakov".equalsIgnoreCase(name)) return "雅科夫";
        return name;
    }
}
