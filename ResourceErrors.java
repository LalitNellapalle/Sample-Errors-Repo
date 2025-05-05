import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

public class ResourceErrors {

    // Resource leak: doesn't close file resources
    public static String readFileWithLeak(String fileName) {
        StringBuilder content = new StringBuilder();
        try {
            // Resource leak: BufferedReader and FileReader are never closed
            BufferedReader reader = new BufferedReader(new FileReader(fileName));
            String line;
            while ((line = reader.readLine()) != null) {
                content.append(line).append("\n");
            }
            // Missing reader.close()
        } catch (IOException e) {
            System.err.println("Error reading file: " + e.getMessage());
        }
        return content.toString();
    }

    // Null pointer exception: doesn't check for null
    public static int getStringLength(String text) {
        // Should check if text is null before calling length()
        return text.length();  // Will throw NullPointerException if text is null
    }

    // Resource leak: database connection not closed
    public static List<String> queryDatabaseWithLeak(String connectionString, String query) {
        List<String> results = new ArrayList<>();
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        
        try {
            conn = DriverManager.getConnection(connectionString);
            stmt = conn.createStatement();
            rs = stmt.executeQuery(query);
            
            while (rs.next()) {
                results.add(rs.getString(1));
            }
            
            // Resources not closed properly in finally block
            
        } catch (SQLException e) {
            System.err.println("Database error: " + e.getMessage());
        }
        
        return results;
    }

    // Null pointer exception: unsafe array access
    public static void processArray(String[] items) {
        // Should check if items is null and has elements
        System.out.println("First item: " + items[0]);  // NullPointerException if items is null
        
        for (int i = 0; i < items.length; i++) {
            // Should check if individual items are null
            System.out.println("Item length: " + items[i].length());  // NullPointerException if any item is null
        }
    }

    // Resource leak and null pointer combo
    public static void complexMethod(String fileName, List<String> dataList) {
        FileReader fileReader = null;
        
        try {
            fileReader = new FileReader(fileName);
            char[] buffer = new char[1024];
            fileReader.read(buffer);
            
            // Potential NPE: doesn't check if dataList is null
            dataList.add(new String(buffer));  // Will throw NullPointerException if dataList is null
            
            // Missing finally block to close fileReader
            
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        System.out.println("Starting error examples program");
        
        // Resource leak examples
        readFileWithLeak("nonexistent_file.txt");  // Resource leak even with exception
        queryDatabaseWithLeak("jdbc:mysql://localhost/test", "SELECT * FROM users");  // Resource leak
        
        // Uncomment to test null pointer exceptions (will crash)
        // String nullString = null;
        // int length = getStringLength(nullString);  // Will throw NullPointerException
        
        // String[] nullArray = null;
        // processArray(nullArray);  // Will throw NullPointerException
        
        System.out.println("Program completed successfully");
    }
}