public class Nonrepeatingchar {
public static char firstNonRepeating(String str) {
        for (int i = 0; i < str.length(); i++) {
            boolean Repeat = false;
        for (int j = 0; j < str.length(); j++) {
                if (i != j && str.charAt(i) == str.charAt(j)) {
                    Repeat = true;
                    break;
            }
}
if (!Repeat) {
                return str.charAt(i);
            }
        }

        return '\0';      }

    public static void main(String[] args) {
        String input = "swiss";
        System.out.println("First non-repeating character: " + FirstNonRepeating(input));
    }
}
